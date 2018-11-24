from alignmentToGenome import localAlignment, retrace
from mapQueryToGenome import mapQueryToGenome, reverseComplement
from indexGenome import createIndex

def callAlignment(genome, hits, query, gap):
    # alignment is a tuple that contains the aligned strings as results
    # best_score keeps track of the best possible alignment
    # best_loc keep track of localization of where alignment starts for best alignment
    alignment = ()
    best_score = 0
    best_loc = 0
    reverse_complement_query = reverseComplement(query)

    for i in hits:
        hom_area = genome[abs(i)-10:abs(i)+10]
        print(hom_area)
        if i < 0:
            result_local_alignment = localAlignment(hom_area, reverse_complement_query, gap)
            if result_local_alignment[0] > best_score:
                alignment = retrace(result_local_alignment[2], result_local_alignment[1], hom_area, query, -10)
                best_score = result_local_alignment[0]
                best_loc = abs(i) - 10
            
        else:
            result_local_alignment = localAlignment(hom_area, query, gap)
            if result_local_alignment[0] > best_score:
                alignment = retrace(result_local_alignment[2], result_local_alignment[1], hom_area, query, -10)
                best_score = result_local_alignment[0]
                best_loc = abs(i) - 10

    return alignment, best_loc


"""
k = 3

stringA = 'ACTACAATATTCGACCGAGTAGGGCACGATGTGAGTCA'

stringB = 'GGCACGA'

index = createIndex(stringA, 3)

hits = mapQueryToGenome(index, k, stringB)

print(index, hits)

results = callAlignment(stringA, hits, stringB, -10)

print(results[0])
print(results[1])
"""