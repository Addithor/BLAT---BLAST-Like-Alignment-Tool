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
#commonIndexes(indexDict)

for i in range(len(querys)):
    listOfHits = mapQueryToGenome(indexDict, k, querys[i])

    print(listOfHits)

    results = callAlignment(genome, listOfHits, querys[i], -1)

    for item in results:
        print(item, end='\n')
        print('', end='\n')
