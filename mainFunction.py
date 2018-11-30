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

k = 11
indexDict = {}
indexDict = createIndex(genome, k)
#commonIndexes(indexDict)

for i in range(len(querys)):
        listOfHits = mapQueryToGenome(indexDict, k, querys[i])

        results = []

        results = callAlignment(genome, listOfHits, querys[i], -1)
        if not results:
                print('alignment not found!')
                continue

        print(end='\n')
        print('block    score   start     span   end       strand')
        print('--------------------------------------------------')

        i = 1
        for item in results:
                print('{0:2d} {1:10d} {2:10d} {3:6d} {4:9d} {5} {6}' .format(i, item[1], item[0][2], item[3], item[0][2] + item[3], '   ', item[2], end='\n'))
                i += 1

        