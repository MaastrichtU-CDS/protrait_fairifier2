import json

from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd


class QueryEngine:
    def __init__(self, serviceLocation):
        self.__serviceLocation = serviceLocation
    
    def query_from_file(self, fileName):
        with open(fileName, 'r') as file:
            query = file.read().replace('\n', ' ')
        return self.get_sparql_dataframe(query)

    def get_sparql_dataframe(self, query):
        """
        Helper function to convert SPARQL results into a Pandas data frame.
        """
        sparql = SPARQLWrapper(self.__serviceLocation)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        result = sparql.query()

        processed_results = json.load(result.response)
        cols = processed_results['head']['vars']

        out = []
        for row in processed_results['results']['bindings']:
            item = []
            for c in cols:
                item.append(row.get(c, {}).get('value'))
            out.append(item)

        df = pd.DataFrame(out, columns=cols)

        if len(processed_results['results']['bindings']) > 0:
            firstRow = processed_results['results']['bindings'][0]
            for c in cols:
                varType = firstRow.get(c,{}).get("type")
                if varType == "uri":
                    df[c] = df[c].astype("category")
                if varType == "literal" or varType == "typed-literal":
                    dataType = firstRow.get(c,{}).get("datatype")
                    if dataType=="http://www.w3.org/2001/XMLSchema#int":
                        df[c] = pd.to_numeric(df[c], errors='coerce')
                    if dataType=="http://www.w3.org/2001/XMLSchema#integer":
                        df[c] = pd.to_numeric(df[c], errors='coerce')
                    if dataType=="http://www.w3.org/2001/XMLSchema#double":
                        df[c] = pd.to_numeric(df[c], errors='coerce')
                    if dataType=="http://www.w3.org/2001/XMLSchema#string":
                        df[c] = df[c].astype("category")
        
        return df