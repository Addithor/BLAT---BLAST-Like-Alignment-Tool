import sys, collections, math, random
import numpy as np
from indexGenome import createIndex

def mapQueryToGenome(index, k, query):
    # List for hits
    hits = []

    # Roll through the query and append to the hits list
    # Positive indexes indicate hits on the leading strand
    # Negative indexes indicate hits on the lagging strand
    for i in range(len(query) - k + 1):
        if index.get(query[i: i+k]):
            hits = hits + index[query[i: i+k]]
        if index.get(reverse_complement(query[i: i+k])):
            for item in index[reverse_complement(query[i: i+k])]:
                hits.append(-item)
    
    return sorted(hits)



def reverse_complement(pattern):
    # Create a list that holds the reverse complement
    new_string = []
    # Create the pattern backwards
    backwards = pattern[::-1]

    # Loop through each base in the reversed string and replace with the comlement basepair 
    for base in backwards:
        if base == "A" or base == "a":
            new_string.append("T")
        elif base == "G" or base == "g":
            new_string.append("C")
        elif base == "C" or base == "c":
            new_string.append("G")
        else:
            new_string.append("A")
    
    new_string = ''.join(new_string)

    return new_string




string = 'AAATTTCCCGGGAAATTT'
k = 3

index = collections.defaultdict()

index = createIndex(string, k)

print(mapQueryToGenome(index, k, 'AAA'))
