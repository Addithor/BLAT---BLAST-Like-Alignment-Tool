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
            hits = hits + index[query[i: i+k]]
        if index.get(reverseComplement(query[i: i+k])):
            for item in index[reverseComplement(query[i: i+k])]:
                hits.append(-item)

    test = True
    while test:
        for i in hits:
            for j in hits:
                test = False
                if not(i == j) and abs(abs(i) - abs(j)) < len(2 * query) and i < 0 and j < 0:
                    hits.remove(i)
                    hits.remove(j)
                    hits.append(int(-(i+j)/2))
                    test = True
                    break
                elif not(i == j) and abs(abs(i) - abs(j)) < len(query) and i > 0 and j > 0:
                    hits.remove(i)
                    hits.remove(j)
                    hits.append(int((i+j)/2))
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