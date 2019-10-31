# -*- coding: utf-8 -*-
# This file is part of hcga.
#
# Copyright (C) 2019, 
# Robert Peach (r.peach13@imperial.ac.uk), 
# Alexis Arnaudon (alexis.arnaudon@epfl.ch), 
# https://github.com/ImperialCollegeLondon/hcga.git
#
# hcga is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hcga is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with hcga.  If not, see <http://www.gnu.org/licenses/>.

import pandas as pd
import numpy as np
import networkx as nx

class Clustering():
    """
    Clustering class
    """    
    
    def __init__(self, G):
        self.G = G
        self.feature_names = []
        self.features = {}

    def feature_extraction(self):

        """Compute the various clustering measures.

        Parameters
        ----------
        G : graph
           A networkx graph

        Returns
        -------
        feature_list : dict
           Dictionary of features related to node clustering.


        Notes
        -----
        Implementation of networkx code:
            `Networkx_clustering <https://networkx.github.io/documentation/stable/reference/algorithms/clustering.html>`_

        We followed the same structure as networkx for implementing clustering features.

        """
        


        G = self.G

        feature_list = {}
        
        
        if not nx.is_directed(G):
            # Calculating number of triangles
            feature_list['num_triangles']=np.asarray(list(nx.triangles(G).values())).mean()
                
            # graph transivity
            C = nx.transitivity(G)
            feature_list['transitivity'] = C
        else:
            feature_list['num_triangles'] = np.nan
            feature_list['transitivity'] = np.nan
        

        # Average clustering coefficient
        feature_list['clustering_mean']=nx.average_clustering(G)
        feature_list['clustering_std']=np.asarray(list(nx.clustering(G).values())).std()
        feature_list['clustering_median']=np.median(np.asarray(list(nx.clustering(G).values())))


        # generalised degree
        feature_list['square_clustering_mean']=np.asarray(list(nx.square_clustering(G).values())).mean()
        feature_list['square_clustering_std']=np.asarray(list(nx.square_clustering(G).values())).std()
        feature_list['square_clustering_median']=np.median(np.asarray(list(nx.square_clustering(G).values())))
        

        


        self.features = feature_list
