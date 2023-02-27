# -*- coding: utf-8 -*-

import os
from rdflib import Graph


if __name__ == '__main__':
    # Load ProTRAIT local concepts
    cwd = os.getcwd()
    path = os.path.join(cwd, 'ontologies')
    terminology = 'proTRAITTermmapperValueTriples.ttl'
    file = os.path.join(path, terminology)
    g = Graph()
    g.parse(file)

    # Save local terminologies as XML
    output_file = os.path.join(path, 'protrait.owl')
    g.serialize(destination=output_file, format='xml')
