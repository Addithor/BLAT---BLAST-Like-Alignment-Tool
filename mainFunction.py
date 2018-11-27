from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio import pairwise2

from readSubseqFile import readGenome
from readTranscriptsFile import readQuery
from indexGenome import createIndex
from mapQueryToGenome import mapQueryToGenome, reverseComplement
from callAlignment import callAlignment
from alignmentToGenome import localAlignment, makeMatrix, similarityMatrix, retrace
from commonIndexes import commonIndexes

genome = readGenome("data/subseq.fasta")
querys = readQuery("data/transcripts.fasta")

k = 15
indexDict = {}
indexDict = createIndex(genome, k)
"""
# creates indexes from genome. Returns dictionary with the indexes
indexDict = createIndex(genome, k)
#commonIndexes(indexDict)
print(querys)
for i in range(1, len(querys)):
    listOfHits = mapQueryToGenome(indexDict, k, querys[i])
    
    print(listOfHits, len(listOfHits), len(querys[i]))
    
    results = callAlignment(genome, listOfHits, querys[i], -1, len(querys[i]) * 2)
    
    print(results[0][0])
    print(results[0][1])
    print(results[1])

    listOfHits = []
"""
"""for i in querys:
    print(i)"""
# finds the locations where k-mer from the query fits to the genome
# returns an integer list with the positions of the hits
"""listOfHits1 = mapQueryToGenome(indexDict, k, querys[0])
print(listOfHits1)
listOfHits2 = mapQueryToGenome(indexDict, k, querys[1])
print(listOfHits2)
listOfHits3 = mapQueryToGenome(indexDict, k, querys[2])
print(listOfHits3)"""
listOfHits4 = mapQueryToGenome(indexDict, k, querys[3])
print(listOfHits4)
listOfHits5 = mapQueryToGenome(indexDict, k, querys[4])
print(listOfHits5)
listOfHits6 = mapQueryToGenome(indexDict, k, querys[5])
print(listOfHits6)
listOfHits7 = mapQueryToGenome(indexDict, k, querys[6])
print(listOfHits7)
listOfHits8 = mapQueryToGenome(indexDict, k, querys[7])
print(listOfHits8)
listOfHits9 = mapQueryToGenome(indexDict, k, querys[8])
print(listOfHits9)
listOfHits10 = mapQueryToGenome(indexDict, k, querys[9])
print(listOfHits10)
listOfHits11 = mapQueryToGenome(indexDict, k, querys[10])
print(listOfHits11)
listOfHits12 = mapQueryToGenome(indexDict, k, querys[11])
print(listOfHits12)
listOfHits13 = mapQueryToGenome(indexDict, k, querys[12])
print(listOfHits13)
listOfHits14 = mapQueryToGenome(indexDict, k, querys[13])
print(listOfHits14)
# returns the best alignment
#results1 = callAlignment(genome, listOfHits1, querys[0], -1, len(querys[0])*2)
#print(results1)
"""
results2 = callAlignment(genome, listOfHits1, querys[1], -1, len(querys[1]))
results3 = callAlignment(genome, listOfHits1, querys[2], -1, len(querys[2]))
"""
results4 = callAlignment(genome, listOfHits4, querys[3], -1, len(querys[3]))
print(results4)
results5 = callAlignment(genome, listOfHits5, querys[4], -1, len(querys[4]))
print(results5)
results6 = callAlignment(genome, listOfHits6, querys[5], -1, len(querys[5]))
print(results6)
results7 = callAlignment(genome, listOfHits7, querys[6], -1, len(querys[6]))
print(results7)
results8 = callAlignment(genome, listOfHits8, querys[7], -1, len(querys[7]))
print(results8)
results9 = callAlignment(genome, listOfHits9, querys[8], -1, len(querys[8]))
print(results9)
results10 = callAlignment(genome, listOfHits10, querys[9], -1, len(querys[9]))
print(results10)
results11 = callAlignment(genome, listOfHits11, querys[10], -1, len(querys[10]))
print(results11)
results12 = callAlignment(genome, listOfHits12, querys[11], -1, len(querys[11]))
print(results12)
results13 = callAlignment(genome, listOfHits13, querys[12], -1, len(querys[12]))
print(results13)
results14 = callAlignment(genome, listOfHits14, querys[13], -1, len(querys[13]))
print(results14)
"""
final1_local_alignment = localAlignment(genome, querys[0], -1)
final1 = retrace(final1_local_alignment[2], final1_local_alignment[1], genome, querys[0], -1)
#print(final1[0])
#print(final1[1])
"""