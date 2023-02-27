# -*- coding: utf-8 -*-

import os
import types

from owlready2 import *
from ontoply.sub_ontology import SubOntology


if __name__ == '__main__':
    # Load ROO
    cwd = os.getcwd()
    path = os.path.join(cwd, 'ontologies')
    onto_path.append(path)
    roo = get_ontology('roo.owl')
    roo.load()

    # Create sub-ontology
    subonto_iri = 'http://test.org/onto.owl'
    subonto = SubOntology(ontology=roo, subonto_iri=subonto_iri)

    # Extract concepts from main ontology and remove children classes
    concepts_list = [
        'Marital Status', 'Smoking Status', 'Radiation Therapy',
        'Clinics and Hospitals'
    ]
    subonto.add_concepts_list(concepts_list, children=False)

    # Save subset of ROO
    output_file = os.path.join(path, 'roo_new.owl')
    output_format = 'rdfxml'
    subonto.save(output_file=output_file, output_format=output_format)

    # Load subset of ROO
    subroo = get_ontology('roo_new.owl')
    subroo.load()

    # Add extra concepts
    concepts_list = [
        'planningComparisonOutcome',
        'reasonNegativeProtonTherapyWithPositivePlanningComparison',
        'reasonProtonOther',
        'timeStoppedSmoking'
    ]
    concepts_labels = [
        'Planning Comparison Outcome',
        'Reason Negative Proton Therapy With Positive Planning Comparison',
        'Reason Proton Other',
        'Time Stopped Smoking'
    ]
    for i in range(len(concepts_list)):
        with subroo:
            types.new_class(concepts_list[i], (Thing,))
            subroo[concepts_list[i]].label = concepts_labels[i]

    # Save modified ROO
    output_file = os.path.join(path, 'roo_new.owl')
    output_format = 'rdfxml'
    subroo.save(file=output_file, format=output_format)
