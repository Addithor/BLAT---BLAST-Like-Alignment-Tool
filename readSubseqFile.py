from Bio.SeqIO.FastaIO import SimpleFastaParser

# function that reads in data from a fasta-file and returns a genome string
def readGenome(file):
    genome = ""
    with open(file, 'r') as f:
        for title, seq in SimpleFastaParser(f):
            genome = seq
    return genome

# print(readGenome("../data/subseq.fasta"))
