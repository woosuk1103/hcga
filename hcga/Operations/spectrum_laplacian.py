#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:41:52 2019

@author: robert
"""


import numpy as np
import networkx as nx


class SpectrumLaplacian():
    """
    Force centrality class
    """
    def __init__(self, G):
        self.G = G
        self.feature_names = []
        self.features = {}

    def feature_extraction(self):

        """Compute ...



        Parameters
        ----------
        G : graph
          A networkx graph




        Returns
        -------



        Notes
        -----



        """

        
        
        G = self.G

        feature_list = {}         
        

        # laplacian spectrum
        eigenvals_L = np.real(nx.linalg.spectrum.laplacian_spectrum(G))
        
        if len(eigenvals_L) < 10:
            eigenvals_L = np.concatenate((eigenvals_L,np.zeros(10-len(eigenvals_L))))        
            
        
        feature_list['algebraic_connectivity']=nx.algebraic_connectivity(G)

        try: 
            # computing with weights
            fiedler_vector = nx.fiedler_vector(G,weight='weight') # can use None
            
            # nodes in spectral partition by fiedler vector
            feature_list['fiedler_vector_neg']=sum(1 for number in fiedler_vector if number <0)
            feature_list['fiedler_vector_pos']=sum(1 for number in fiedler_vector if number >0)
            feature_list['fiedler_vector_ratio_neg_pos']=sum(1 for number in fiedler_vector if number <0)/sum(1 for number in fiedler_vector if number >0)
        except:
                    # nodes in spectral partition by fiedler vector
            feature_list['fiedler_vector_neg']=np.nan
            feature_list['fiedler_vector_pos']=np.nan
            feature_list['fiedler_vector_ratio_neg_pos']=np.nan
        
     
        for i in range(10):               
            feature_list['L_eigvals_'+str(i)]=eigenvals_L[i]
        
        
        for i in range(10):
            for j in range(10):
                try:
                    feature_list['L_eigvals_ratio_'+str(i)+'_'+str(j)] = eigenvals_L[i]/eigenvals_L[j]
                except:
                    feature_list['L_eigvals_ratio_'+str(i)+'_'+str(j)] = np.nan
                
        feature_list['L_eigvals_min'] = min(eigenvals_L)




        

        self.features = feature_list