from alignmentToGenome import localAlignment, retrace
from mapQueryToGenome import mapQueryToGenome, reverseComplement
from indexGenome import createIndex

def callAlignment(genome, hits, query, gap, size_hom_area):
    # alignment is a tuple that contains the aligned strings as results
    # best_score keeps track of the best possible alignment
    # best_loc keep track of localization of where alignment starts for best alignment
    alignment = ()
    best_score = 0
    best_loc = 0
    reverse_complement_query = reverseComplement(query)
    dist = int(size_hom_area / 2)
    temp_loc = 0

    for i in hits:

        if abs(i) - dist < 0:
            hom_area = genome[0:abs(i)+dist]
            temp_loc = 0
        elif abs(i) + dist > len(genome):
            hom_area = genome[abs(i)-dist:len(genome)]
            temp_loc = abs(i)-dist
        else:
            hom_area = genome[abs(i)-dist:abs(i)+dist]
            temp_loc = abs(i)-dist

        if i < 0:
            result_local_alignment = localAlignment(hom_area, reverse_complement_query, gap)
            if result_local_alignment[0] > best_score:
                alignment = retrace(result_local_alignment[2], result_local_alignment[1], hom_area, query, gap)
                best_score = result_local_alignment[0]
                best_loc = temp_loc

        else:
            result_local_alignment = localAlignment(hom_area, query, gap)
            if result_local_alignment[0] > best_score:
                alignment = retrace(result_local_alignment[2], result_local_alignment[1], hom_area, query, gap)
                best_score = result_local_alignment[0]
                best_loc = temp_loc

    return alignment, best_loc


"""
k = 3
stringA = 'ACTACCATATTCGA'
stringB = 'CACCATTC'
index = createIndex(stringA, 3)
hits = mapQueryToGenome(index, k, stringB)
print(index, hits)
results = callAlignment(stringA, hits, stringB, -1, 20)
print(results[0])
print(results[1])
"""
