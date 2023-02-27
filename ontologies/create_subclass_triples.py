#!/usr/bin/env python
# coding: utf-8
import re
import rdflib
import codecs

import pandas as pd
import numpy as np

from string import Template
from tabulate import tabulate


urlItemList = "https://github.com/ProTraitInfra/Item-lists/blob/main/Lists/Definitieve%20CRF's%20OpenClinica/Generic/Generic%202/PROTRAIT_GENERIC.xls?raw=true"
df = pd.read_excel(urlItemList,sheet_name="Items", usecols=["ITEM_NAME*", "DESCRIPTION_LABEL*", "RESPONSE_OPTIONS_TEXT", "RESPONSE_VALUES_OR_CALCULATIONS"])

#rename column names
df = df.rename(columns={'ITEM_NAME*': 'ItemName', 'DESCRIPTION_LABEL*': 'ItemDescription', 'RESPONSE_OPTIONS_TEXT':'ValueStringList', 'RESPONSE_VALUES_OR_CALCULATIONS' : "ValueIntegerList" })
#change all NaN to none values
df = df.replace({np.nan: None})
#remove from the in valueStringList column the commas with escape used in the excel: "\\,"
df['ValueStringList']=df.ValueStringList.replace({r"\\\\," : "_"}, regex=True)
#remove special characters in valueStringList column for categorical values
df['ValueStringList']=df.ValueStringList.replace({"[^0-9a-zA-Z,\s-]+": ""},regex=True)


#create a class for continous variables. extract columns from df and enter in the template shacle
class CreateTermMappingValueTriples:
    def __init__(self, ItemName, OntologyClass, ItemDescription, ValueStringList, ValueIntegerList):
        """
        The CreateTermMappingValueTriples class creates the triples needed to select values for the categorical variables in the term mapper .

        Input parameters:
            self:  
            ItemName = ProTRAIT name of the item 
            ItemDescription = human readable description of the variable
            OntologyClass = ontology uri of the item from the r2rml file
            ValueStringList = list of possible values in string format
            ValueStringList = list of corresponding integer values for libre clinica
        """
        self.ItemName = ItemName
        self.OntologyClass = OntologyClass
        self.ItemDescription = ItemDescription
        self.ValueStringList = ValueStringList
        self.ValueIntegerList = ValueIntegerList

    def triples(self):
        """
        Triples function  creates the triples needed to select values for the categorical variables in the term mapper .
        """
        
        #add optional rangeMax shacle shape
        ValueTriples = ""
        ValueList = []
        triples = []
        
        #creating lists from the value option columns
        stringList = self.ValueStringList.split(",")
        integerList = self.ValueIntegerList.split(",")
        
        #removing spaces in the list
        stringList = [item.lstrip() for item in stringList]
        stringList = [item.replace(' ', '_') for item in stringList]
        print("#", stringList, integerList)

        #raise exception if something went wrong    
        if len(stringList) != len(integerList): raise Exception("Unequeal lengths of string and integer lists in " + self.ItemName) 

        #create triples     
        for string, integer in zip(stringList, integerList):
            label = string.replace('_', ' ')
            triple_content = """
protrait:${string}
    rdfs:subClassOf ${ontologyClass};
    rdfs:label '${label}';
    protrait:LC_Code "${integer}"^^xsd:integer.
"""
            triples = Template(triple_content).substitute(
                string=string, ontologyClass=self.OntologyClass,
                label=label, integer=integer
            )
        
            ValueTriples += triples

        return ValueTriples    


graph = rdflib.Graph()
#graph.parse("https://raw.githubusercontent.com/MaastrichtU-CDS/protrait_mapping-unifications/master/GenericList2/GenericList2_stagingDB.ttl", format='ttl')
graph.parse("https://gitlab.com/MatthijsSloep/r2rml_mappings/-/raw/main/GenericList2_stagingDB.ttl", format='ttl')


query = """
PREFIX rr: <http://www.w3.org/ns/r2rml#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ncit: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#>
PREFIX roo: <http://www.cancerdata.org/roo/>

SELECT ?templateURI ?ontologyClass
WHERE {
       ?s rdf:type rr:TriplesMap;
       		rr:subjectMap [
            rr:template ?templateURI;
            rr:class ?ontologyClass;].
}
"""

results = graph.query(query)

columnNames = [str(item) for item in results.vars]
df2 = pd.DataFrame(results, columns=columnNames)

#print(tabulate(df2, headers = 'keys', tablefmt = 'github'))

#extract the proTRAIT item name from the uri 

for index, row in df2.iterrows():
       oldVal = row['templateURI']
       res = re.findall(r'\{.*?\}', row['templateURI'])

       #selects last item in list
       value = res[-1]
       #strips brackets
       result = value[1:-1]
       
       #print(oldVal,result)
       row['templateURI'] = str(row['templateURI']).replace(oldVal,result)
      


#create dictionary with prefixes and uri's
ontologyDict = {
    "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#" : "ncit:",
    "http://www.cancerdata.org/roo/":"roo:", 
    "http://purl.bioontology.org/ontology/STY/" : "sty:", 
    "http://semanticscience.org/resource/SIO_" : "sio:", 
    "http://purl.bioontology.org/ontology/ICD10/" : "icd:", 
    "http://purl.obolibrary.org/obo/UO_" : "uo:",
    "http://www.w3.org/2006/time#" : "time"
}

#loop over dictionary to replace values in df
for key, value in ontologyDict.items():
    df2['ontologyClass'] = df2['ontologyClass'].str.replace(key,value, regex=False)
    
    
#print(tabulate(df2, headers = 'keys', tablefmt = 'github'))


#create a proTRAITTermmapperValueTriples.ttl file  with utf-8 encoding
f = codecs.open("proTRAITTermmapperValueTriples.ttl", "w", "utf-8")

prefixes = """
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix rr: <http://www.w3.org/ns/r2rml#>
prefix ex: <http://example.com/ns#>
prefix map: <http://mapping.local/>
prefix sty: <http://purl.bioontology.org/ontology/STY/>
prefix sio: <http://semanticscience.org/resource/SIO_>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix ncit: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#>
prefix roo: <http://www.cancerdata.org/roo/>
prefix icd: <http://purl.bioontology.org/ontology/ICD10/>
prefix skos: <http://www.w3.org/2008/05/skos#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix uo: <http://purl.obolibrary.org/obo/UO_>
prefix time: <http://www.w3.org/2006/time#>
prefix protrait: <http://www.protrait.nl/> 

"""

f.write(prefixes) 

def getOntologyClass(protraitItemName, df):
    
    ontologyClass = ''

    for index, value in enumerate(df['templateURI']):                 
        if value == protraitItemName:
            ontologyClass = df['ontologyClass'].iloc[index]
            
    return ontologyClass

#write triples 
for i, row in df.iterrows():
    if row['ValueIntegerList'] != None :
        name = row['ItemName'].lower() 
        ontoClass = getOntologyClass(name, df2)
        
        print("#", name, "-", ontoClass)
        if ontoClass != "":
            genericTriples = CreateTermMappingValueTriples(
                row.ItemName, ontoClass, row.ItemDescription, row.ValueStringList, row.ValueIntegerList
                )
            f.write(str(genericTriples.triples()))
f.close()            
            #print(genericTriples.triples())

