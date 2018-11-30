#
# File name: callAlignment.py
# Authors: Arnar Þór Björgvinsson, Unnur Ása Bjarnadóttir, Sóley Lúðvíksdóttir
# Submission: 30.11.2018
# Course: Töl504M
# Instructor: Páll Melsted
# 
# =============================================================================
"""Alignment is a tuple that contains the aligned strings as results, first string 
   in the tuple is the genomic area and the second is the query. Best_score keeps 
   track of the best possible alignment and best_loc keeps track of localization 
   of where alignment starts for the best alignment """
# =============================================================================
# Imports
# =============================================================================

from alignmentToGenome import localAlignment, retrace
from mapQueryToGenome import mapQueryToGenome, reverseComplement
from indexGenome import createIndex

def callAlignment(genome, hits, query, gap):    
    alignment = ()
    score = 0
    loc = 0
    reverse_complement_query = reverseComplement(query) 
    dist = 50
    temp_loc = 0
    strand = ''
    results = []

    for i in hits:
            if abs(i[0]) - dist < 0:
                hom_area = genome[0:abs(i[1])+dist]
                temp_loc = 0
            elif abs(i[1]) + dist > len(genome):
                hom_area = genome[abs(i[0])-dist:len(genome)]
                temp_loc = abs(i[0])-dist
            else:
                hom_area = genome[abs(i[0])-dist:abs(i[1])+dist]
                temp_loc = abs(i[0])-dist

            if i[0] < 0:
                result_local_alignment = localAlignment(hom_area, reverse_complement_query, gap)
                alignment = retrace(result_local_alignment[2], result_local_alignment[1], hom_area, query, gap, temp_loc)
                score = result_local_alignment[0]
                loc = temp_loc
                strand = 'B'
                results.append((alignment, score, strand, len(alignment[0])))
                
            else:
                result_local_alignment = localAlignment(hom_area, query, gap)
                alignment = retrace(result_local_alignment[2], result_local_alignment[1], hom_area, query, gap, temp_loc)
                score = result_local_alignment[0]
                loc = temp_loc
                strand = 'F'
                results.append((alignment, score, strand, len(alignment[0])))
                
    remove = []

    
    for item in results:
        if item[1] < 50:
            remove.append(item)
    
    for item in remove:
        results.remove(item)


    return results

