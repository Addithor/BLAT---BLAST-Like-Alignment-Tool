from Bio.SeqIO.FastaIO import SimpleFastaParser

# fall sem les inn gögn úr fasta-skrá og skilar genome streng
def readGenome(file):
    genome = ""
    with open(file, 'r') as f:
        for title, seq in SimpleFastaParser(f):
            genome = seq
    return genome
