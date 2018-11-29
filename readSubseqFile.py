#
# File name: readSubseqFile.py
# Authors: Arnar Þór Björgvinsson, Unnur Ása Bjarnadóttir, Sóley Lúðvíksdóttir
# Submission: 30.11.2018
# Course: Töl504M
# Instructor: Páll Melsted
# 
# =============================================================================
"""A function that reads in data from a fasta-file and returns a genome string. 
"""
# =============================================================================
# Imports
# =============================================================================

from Bio.SeqIO.FastaIO import SimpleFastaParser

def readGenome(file):
    genome = ""
    with open(file, 'r') as f:
        for title, seq in SimpleFastaParser(f):
            genome = seq
    return genome

# print(readGenome("../data/subseq.fasta"))
