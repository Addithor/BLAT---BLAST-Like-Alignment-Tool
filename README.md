# Implementation of BLAT---BLAST-Like-Alignment-Tool

An implementation of BLAT, a sequence alignment algorithm that performs mRNA/DNA alignments with great accuracy and speed. In this implementation of the algorithm we align a query sequence to a reference sequence from the human genome.

In order to do that, we have to follow a few steps. First of all, we have to create an index of all non-overlapping k-mers in the database to be able to scan through the query sequences. Secondly, we need to scan through each of the queries and create a dictionary that contains the indices of the positions of the hits between the genome and each query string. Lastly we need to find the positions of the best alignments, create an alignment matrix and return the aligned strings that have the best alignment to the genome.

## Getting Started

Option A: clone this repository and get a copy up and running on your local computer. Just hit the clone button and save the link to your clipboard. Then open your command prompt and navigate to the folder where you want to save the project, and type in these commands:
```
git clone https://github.com/Addithor/BLAT---BLAST-Like-Alignment-Tool.git
```

Option B: unzip the project folder and save it in a folder on your computer. 

### Prerequisites

This project is written in Python 3 and uses components from Biopython and Numpy.

To install the latest version of Python 3, go to https://www.python.org/downloads/ and download the .exe file for your operating system. Follow the installation instructions. Too check if the installation completed successfully, run this command:
```
python --version
```
You should see the following line on your command prompt screen: 
```
C:\Users\Notandi>python --version
Python 3.x.x
```
To install Numpy, use the package manager pip that comes automatically with Python 3.x.x, and run this command:
```
pip install numpy
```
To install Biopython, run this command:
```
pip install biopython
```
You might also want to install matplotlib, to install run this command:
```
pip install matplotlib
```

### How to run the implementation

The implementation is divided into functions that perform operations and functions that read in our data sets. The file mainFunction.py pulls everything together and returns the aligned strings, and where the alignment starts in the genome.

Our data, transcripts.fasta and subseq.fasta are taken in as parameters in two different functions. readSubseqFile.py that returns a genome string from the subseq.fasta file and readTranscriptsFile.py that returns a list of queries from the transcripts.fasta file. This makes if easier to work with the given FASTA file format.  

To run:
```
python mainFunction.py
```

## Creators

* **Arnar Þór Björgvinsson** - *Líffræði MS*
* **Unnur Bjarnadóttir** - *Tölvunarfræði BS*
* **Sóley Lúðvíksdóttir** - *Tölvunarfræði BS*

## Author of the original algorithm

* W. James Kent, BLAT---The BLAST-Like ALignment Tool, *Genome Res. 2002 12: 656-664*

