import sys, collections, math, random
import numpy as np
from indexGenome import createIndex

def mapQueryToGenome(index, k, query):
    # List for hits
    hits = []

    for i in range(len(query) - k + 1):
        if index.get(query[i: i+k]):
            print(index[query[i: i+k]])

"""
string = 'AAATTTCCCGGGAAA'
k = 3

index = collections.defaultdict()

index = createIndex(string, k)

mapQueryToGenome(index, k, 'AAA')
"""