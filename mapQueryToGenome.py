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
 
    # Clusters hits together if they are too close
    i = 0
    while i + 1 < len(hits):
        if hits[i][0] > 0 and hits[i+1][0] > 0:
            if hits[i][1] + 100 > hits[i+1][0]:
                hits[i] = (hits[i][0], hits[i+1][1])
                del hits[i+1]
            else:
                i += 1
        elif hits[i][0] < 0 and hits[i+1][0] < 0:
            if hits[i][1] + 100 > hits[i+1][0]:
                hits[i] = (hits[i][0], hits[i+1][1])
                del hits[i+1]
            else:
                i += 1
        else:
            i +=1
        
    # Remove hit if it is not within 100 bp of another hit -> two perfect hits needed to call alignment
    i = 0
    while i < len(hits):
        if (abs(abs(hits[i][0]) - abs(hits[i][1]))) < 2:
            del hits[i]
        else:
            i += 1

 
    return hits



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
