from Bio.SeqIO.FastaIO import SimpleFastaParser

from readSubseqFile import readGenome
from readTranscriptsFile import readQuery
from indexGenome import createIndex
from mapQueryToGenome import mapQueryToGenome, reverseComplement
from callAlignment import callAlignment
from alignmentToGenome import localAlignment, makeMatrix, similarityMatrix, retrace

genome = readGenome("../data/subseq.fasta")
querys = readQuery("../data/transcripts.fasta")

k = 11
indexDict = {}

# creates indexes from genome. Returns dictionary with the indexes
indexDict = createIndex(genome, k)

# finds the locations where k-mer from the query fits to the genome
# returns an integer list with the positions of the hits
listOfHits1 = mapQueryToGenome(indexDict, k, querys[0])
listOfHits2 = mapQueryToGenome(indexDict, k, querys[1])
listOfHits3 = mapQueryToGenome(indexDict, k, querys[2])
listOfHits4 = mapQueryToGenome(indexDict, k, querys[3])
listOfHits5 = mapQueryToGenome(indexDict, k, querys[4])
listOfHits6 = mapQueryToGenome(indexDict, k, querys[5])
listOfHits7 = mapQueryToGenome(indexDict, k, querys[6])
listOfHits8 = mapQueryToGenome(indexDict, k, querys[7])
listOfHits9 = mapQueryToGenome(indexDict, k, querys[8])
listOfHits10 = mapQueryToGenome(indexDict, k, querys[9])
listOfHits11 = mapQueryToGenome(indexDict, k, querys[10])
listOfHits12 = mapQueryToGenome(indexDict, k, querys[11])
listOfHits13 = mapQueryToGenome(indexDict, k, querys[12])
listOfHits14 = mapQueryToGenome(indexDict, k, querys[13])

# returns the best alignment
results1 = callAlignment(genome, listOfHits1, querys[0], -1, len(querys[0]))
#print(results1)

"""
#results2 = callAlignment(genome, listOfHits1, querys[1], -1, len(querys[1]))
#results3 = callAlignment(genome, listOfHits1, querys[2], -1, len(querys[2]))
#results4 = callAlignment(genome, listOfHits1, querys[3], -1, len(querys[3]))
#results5 = callAlignment(genome, listOfHits1, querys[4], -1, len(querys[4]))
#results6 = callAlignment(genome, listOfHits1, querys[5], -1, len(querys[5]))
#results7 = callAlignment(genome, listOfHits1, querys[6], -1, len(querys[6]))
#results8 = callAlignment(genome, listOfHits1, querys[7], -1, len(querys[7]))
#results9 = callAlignment(genome, listOfHits1, querys[8], -1, len(querys[8]))
#results10 = callAlignment(genome, listOfHits1, querys[9], -1, len(querys[9]))
#results11 = callAlignment(genome, listOfHits1, querys[10], -1, len(querys[10]))
#results12 = callAlignment(genome, listOfHits1, querys[11], -1, len(querys[11]))
#results13 = callAlignment(genome, listOfHits1, querys[12], -1, len(querys[12]))
#results14 = callAlignment(genome, listOfHits1, querys[13], -1, len(querys[13]))
"""
final1_local_alignment = localAlignment(genome, querys[0], -1)
final1 = retrace(final1final1_local_alignment[2], final1final1_local_alignment[1], genome, querys[0], -1)
#print(final1[0])
#print(final1[1])
