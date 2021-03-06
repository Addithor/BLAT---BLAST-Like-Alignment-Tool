from alignmentToGenome import localAlignment, retrace
from mapQueryToGenome import mapQueryToGenome, reverseComplement
from indexGenome import createIndex

def callAlignment(genome, hits, query, gap):
    # alignment is a tuple that contains the aligned strings as results, first string in the tuple is the genomic area and the secondis the query
    # best_score keeps track of the best possible alignment
    # best_loc keep track of localization of where alignment starts for best alignment
    alignment = ()
    score = 0
    reverse_complement_query = reverseComplement(query) 
    dist = 50
    temp_loc = 0
    strand = ''
    results = []

    for i in hits:
        # Set the homolog area too which the query is to be compared
        # 50 bp outside the hit area too be included in the alignment
        if abs(i[0]) - dist < 0:
            hom_area = genome[0:abs(i[1])+dist]
            temp_loc = 0
        elif abs(i[1]) + dist > len(genome):
            hom_area = genome[abs(i[0])-dist:len(genome)]
            temp_loc = abs(i[0])-dist
        else:
            hom_area = genome[abs(i[0])-dist:abs(i[1])+dist]
            temp_loc = abs(i[0])-dist

        # If the hit is on the reverse strand (-) perform the alignment  of the reverse compliment
        if i[0] < 0:
            result_local_alignment = localAlignment(hom_area, reverse_complement_query, gap)
            alignment = retrace(result_local_alignment[2], result_local_alignment[1], hom_area, query, gap, temp_loc)
            score = result_local_alignment[0]
            strand = '-'
            results.append((alignment, score, strand, len(alignment[0])))
        # If the hit is on the forward strand (+) perform the alignment as is
        else:
            result_local_alignment = localAlignment(hom_area, query, gap)
            alignment = retrace(result_local_alignment[2], result_local_alignment[1], hom_area, query, gap, temp_loc)
            score = result_local_alignment[0]
            strand = '+'
            results.append((alignment, score, strand, len(alignment[0])))
                
    remove = []

    # If the score of an alignment is less that 50 we remove it
    for item in results:
        if item[1] < 50:
            remove.append(item)
    
    for item in remove:
        results.remove(item)


    return results

