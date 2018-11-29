from Bio.SeqIO.FastaIO import SimpleFastaParser

# function that reads in data from a fasta-file and returns a list with query strings
def readQuery(file):
    query = []
    with open(file, 'r') as f:
        for title, seq in SimpleFastaParser(f):
            query.append(seq)
    return query

#print(readQuery("../data/transcripts.fasta"))
