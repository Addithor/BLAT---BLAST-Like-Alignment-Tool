# Implementation of BLAT---BLAST-Like-Alignment-Tool

An implementation of BLAT, a sequence alignment algorithm that performs mRNA/DNA alignments with great accuracy and speed. In this implementation of the algorithm we align a query sequence to a short reference sequence from the human genome.

## Getting Started

Option A: clone this repository and get a copy up and running on your local computer. Just hit the clone button and save the link to your clipboard. Then open your command prompt and navigate to the folder where you want to save the project, and type in these commands:
```
git clone https://github.com/Addithor/BLAT---BLAST-Like-Alignment-Tool.git
```

Option B: unzip the project folder and save it in a folder on your computer. 

Start working with it!

See deployment for notes on how to deploy the project on your computer.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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

### How to run the implementation

The implementation is divided into functions that perform operations and functions that read in our data sets. The file mainFunction.py pulls everything together and returns a query-string that has the best alignment.

BÆTA VIÐ: hvernig gögnin eru lesin inn í gagna föllin...

To run:
```
python mainFunction.py
```

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eu sapien erat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

End with an example of getting some data out of the algorithm.

## Creators

* **Arnar Þór Björgvinsson** - *Líffræði MS*
* **Unnur Ása Bjarnadóttir** - *Tölvunarfræði BS*
* **Sóley Lúðvíksdóttir** - *Tölvunarfræði BS*

## Author of the original algorithm

* W. James Kent, BLAT---The BLAST-Like ALignment Tool, *Genome Res. 2002 12: 656-664*

