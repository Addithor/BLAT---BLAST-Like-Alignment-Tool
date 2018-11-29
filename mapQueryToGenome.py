#
# File name: mapQueryToGenome.py
# Authors: Arnar Þór Björgvinsson, Unnur Ása Bjarnadóttir, Sóley Lúðvíksdóttir
# Submission: 30.11.2018
# Course: Töl504M
# Instructor: Páll Melsted
# 
# =============================================================================
"""This function goes trough the query string and appends hits to a list.
   Hits are divided with - and + that indicate if they happen on a lagging or
   a leading strand. Then they are clustered together.
"""
# =============================================================================
# Imports
# =============================================================================

import collections
from indexGenome import createIndex

def mapQueryToGenome(index, k, query):
    # List for hits
    hits = []

    # Roll through the query and append to the hits list
    # Positive indexes indicate hits on the leading strand
    # Negative indexes indicate hits on the lagging strand
    for i in range(len(query) - k + 1):
        if index.get(query[i: i+k]):
            for item in index[query[i: i+k]]:
                hits.append((item, item+1))
        if index.get(reverseComplement(query[i: i+k])):
            for item in index[reverseComplement(query[i: i+k])]:
                hits.append((-item, -item-1))

    hits = sorted(removeDuplicates(hits))

    # Remove lone-standing hits from hits list
    i = 0
    while i < len(hits):
        if i < 1 and not(abs(abs(hits[i][0]) - abs(hits[i+1][0])) < 100000):
            hits.remove(hits[i])
        elif i > len(hits) - 1 and not(abs(abs(hits[i][0]) - abs(hits[i-1][0])) < 100000):
            hits.remove(hits[i])
        elif i < len(hits) - 1 and i >= 1 and not(abs(abs(hits[i][0]) - abs(hits[i-1][0])) < 100000 or abs(abs(hits[i][0]) - abs(hits[i+1][0])) < 100000):
            hits.remove(hits[i])
        i += 1
 
    # Clusters hits together if they are too close
    test = True
    while test:
        for i in hits:
            for j in hits:
                test = False
                if i[0] > 0 and j[0] > 0 and i[0] < j[0] and abs(abs(i[1]) - abs(j[0])) < 500:
                    hits.append((i[0], j[1]))
                    hits.remove(i)
                    hits.remove(j)
                    test = True
                    break
                elif i[0] < 0 and j[0] < 0 and i[0] > j[0] and abs(abs(i[1]) - abs(j[0])) < 500:
                    hits.append((i[1], j[0]))
                    hits.remove(i)
                    hits.remove(j)
                    test = True
                    break
 
    return sorted(removeDuplicates(hits))



def reverseComplement(pattern):
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

def removeDuplicates(hits):
    # Removes duplicates from lists
    final_list = []
    for num in hits:
        if num not in final_list:
            final_list.append(num)
    return final_list



"""
string = 'ATGAGAAGAGATATGAGTTGTGAGAGAGTGAGAATGATGGAGGGAG'
k = 3

index = collections.defaultdict()

index = createIndex(string, k)

hits = mapQueryToGenome(index, k, 'AGAAA')

print(hits)
"""