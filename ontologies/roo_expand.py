# -*- coding: utf-8 -*-

import os
import types

from owlready2 import *


if __name__ == '__main__':
    # Create empty ontology
    base_iri = 'http://test.org/'
    onto = get_ontology(base_iri)

    # Add concepts
    concepts_list = [
        'planningComparisonOutcome',
        'reasonNegativeProtonTherapyWithPositivePlanningComparison',
        'reasonProtonOther'
    ]
    concepts_labels = [
        'Planning Comparison Outcome',
        'Reason Negative Proton Therapy With Positive Planning Comparison',
        'Reason Proton Other'
    ]
    for i in range(len(concepts_list)):
        with onto:
            types.new_class(concepts_list[i], (Thing,))
            onto[concepts_list[i]].label = concepts_labels[i]

    # Save ontology
    cwd = os.getcwd()
    path = os.path.join(cwd, 'ontologies')
    output_file = os.path.join(path, 'roo_new.owl')
    output_format = 'rdfxml'
    onto.save(file=output_file, format=output_format)

    # Changing namespace forcefully in the output
    new_iri = 'http://www.cancerdata.org/roo/'
    with open(output_file, 'r') as file:
        content = file.read()
        content = content.replace(base_iri, new_iri)
    with open(output_file, 'w') as file:
        file.write(content)
