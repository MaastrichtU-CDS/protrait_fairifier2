# -*- coding: utf-8 -*-

"""
Module with R2RML functionalities
"""

import os
from SPARQLWrapper import SPARQLWrapper
from rdflib import Graph


class ManageR2RML:
    """ Management of RDF mappings
    """

    def __init__(self, graphdb_base_url, r2rml_endpoint, mapping_file):
        """ Initialisation method for ManageR2RML class

        Parameters
        ----------
        graphdb_base_url : str
            GraphDB endpoint
        r2rml_endpoint : str
            R2RML endpoint
        mapping_file : str
            Path to mapping file
        """
        self.graphdb_base_url = graphdb_base_url
        self.r2rml_endpoint = r2rml_endpoint
        self.mapping_file = mapping_file

    def drop_rdf_mappings(self):
        """ Drop all RDF mappings
        """
        try:
            url = os.path.join(self.graphdb_base_url, self.r2rml_endpoint)
            endpoint = SPARQLWrapper(url)
            endpoint.setQuery('DROP ALL;')
            endpoint.method = 'POST'
            endpoint.query()
        except Exception as e:
            raise Exception(f'Unable to drop RDF mappings: {e}')

    def load_rdf_mapping(self):
        """ Load RDF mapping file
        """
        try:
            g = Graph()
            g.parse(self.mapping_file, format='n3')
            self.rdf_string = g.serialize(format='nt')
        except Exception as e:
            raise Exception(f'Unable to load RDF mapping: {e}')

    def insert_rdf_mapping(self):
        """ Insert RDF mapping to R2RML endpoint
        """
        try:
            url = os.path.join(self.graphdb_base_url, self.r2rml_endpoint)
            endpoint = SPARQLWrapper(url)
            insert_query = 'INSERT { %s } WHERE { }' % self.rdf_string
            endpoint.setQuery(insert_query)
            endpoint.method = 'POST'
            endpoint.query()
        except Exception as e:
            raise Exception(f'Unable to insert RDF mapping: {e}')
