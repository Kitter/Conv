#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gensim.models import word2vec
import MeCab
import sys
import networkx
import simplejson as json


class ConvergentJP:
    def __init__(self, model):
        self.model = model
        self.graph = networkx.DiGraph()
        d = json.load(open('graphJP.json'))
        self.graph.add_nodes_from(d['nodes'])
        self.graph.add_edges_from(d['edges'])
    
    def relation(self, param1, param2):
        self.graph.remove_edge(param1, param2)
        data = networkx.dijkstra_path(self.graph, param1,param2)
        weight = pow(1 - self.model.similarity(param1, param2),2)
        self.graph.add_edge(param1, param2, weight=weight)
        for x in data:
            print(x)

# English Version
class ConvergentEN:
    def __init__(self, model):
        self.model = model


if __name__ == "__main__":
    modelJP = word2vec.Word2Vec.load('./model/jp_wiki')
    convJP = ConvergentJP(modelJP)
    convJP.relation(sys.argv[1], sys.argv[2])