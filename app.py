#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gensim.models import word2vec
import MeCab
import sys
import networkx


class Network:
    def __init__(self, model):
        self.model = model

class Game:
    def __init__(self, model):
        self.model = model
        self.vocb = model.vocab.kyes()


if __name__ == "__main__":
    model = word2vec.Word2Vec.load('./model/jp_wiki')