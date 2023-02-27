# -*- coding: utf-8 -*-

import os
from owlready2 import *


if __name__ == '__main__':
    # Load ProTRAIT local concepts
    base_url = 'https://raw.githubusercontent.com/MaastrichtU-CDS/'
    protrait = 'protrait_term-mapper/main/'
    terminology = 'proTRAITTermmapperValueTriples.ttl'
    url = os.path.join(base_url, protrait, terminology)
    protrait = get_ontology(url)
    protrait.load()

    # Save local terminologies as XML
    cwd = os.getcwd()
    path = os.path.join(cwd, 'ontologies')
    output_file = os.path.join(path, 'protrait.owl')
    output_format = 'rdfxml'
    protrait.save(file=output_file, format=output_format)
