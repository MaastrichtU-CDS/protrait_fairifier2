# -*- coding: utf-8 -*-

import os
from owlready2 import *
from ontoply.sub_ontology import SubOntology


if __name__ == '__main__':
    # Load NCIT ontology
    cwd = os.getcwd()
    path = os.path.join(cwd, 'ontologies')
    onto_path.append(path)
    ncit = get_ontology('ncit.owl')
    ncit.load()

    # Create sub-ontology
    subonto_iri = 'http://test.org/onto.owl'
    subonto = SubOntology(ontology=ncit, subonto_iri=subonto_iri)

    # Extract concepts from main ontology and add to sub-ontology
    concepts_list = [
        'Education Level', 'Neoplasm by Site', 'Alcohol Use History'
    ]
    subonto.add_concepts_list(concepts_list)

    # Save sub-ontology extracted
    output_file = os.path.join(path, 'subncit.owl')
    output_format = 'rdfxml'
    subonto.save(output_file, output_format)
