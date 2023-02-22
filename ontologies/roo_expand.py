# -*- coding: utf-8 -*-

import os
import types

from owlready2 import *


if __name__ == '__main__':
    # Load ROO
    cwd = os.getcwd()
    path = os.path.join(cwd, 'ontologies')
    onto_path.append(path)
    roo = get_ontology('roo.owl')
    roo.load()

    # Adding Maastro Clinic as a concept
    parent_label = 'Clinics and Hospitals'
    parent_concept = roo.search(label=parent_label)[0]
    concept = 'MaastroClinic'
    concept_label = 'Maastro Clinic'
    with roo:
        types.new_class(concept, (parent_concept,))
        roo[concept].label = concept_label

    # Add extra concepts
    # TODO: do these concepts have children? what are the parents?
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
        with roo:
            types.new_class(concepts_list[i], (Thing,))
            roo[concepts_list[i]].label = concepts_labels[i]

    # Save modified ROO
    output_file = os.path.join(path, 'roo_new.owl')
    output_format = 'rdfxml'
    roo.save(file=output_file, format=output_format)
