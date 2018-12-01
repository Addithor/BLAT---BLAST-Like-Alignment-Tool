from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio import pairwise2
import timeit

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

total_time = 0
j = 0
for i in range(len(querys)):
        start = timeit.default_timer()
        listOfHits = mapQueryToGenome(indexDict, k, querys[i])

        results = []

        results = callAlignment(genome, listOfHits, querys[i], -1)
        if not results:
                print('alignment not found!')
                j += 1
                continue

        print(end='\n')
        print('block    score   start     span   end       strand')
        print('--------------------------------------------------')

        i = 1
        j += 1
        for item in results:
                print('{0:2d} {1:10d} {2:10d} {3:6d} {4:9d} {5} {6}' .format(i, item[1], item[0][2], item[3], item[0][2] + item[3], '   ', item[2], end='\n'))
                i += 1

        stop = timeit.default_timer()
        time = (stop - start)
        print('Runtime for query number ', j, ': ', '{0:2.3f}' .format(time), 's') 
        total_time += time

print(end='\n')        
print('Total runtime for all queries: ', '{0:2.3f}' .format(total_time), 's') 
