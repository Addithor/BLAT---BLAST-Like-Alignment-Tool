from indexGenome import createIndex
import matplotlib.pyplot as plt

def commonIndexes(index):
    most_indexes = 0

    for key, value in index.items():
        if len(value) > most_indexes:
            most_indexes = len(value)
    
    l = [0] * most_indexes

    for key, value in index.items():
        l[len(value)-1] += 1
    
    i = 0
    while i < len(l):
        if l[i] == 0:
            del l[i]
        i += 1
    
    
    plt.plot(l)
    plt.show()


"""
commonIndexes(createIndex('ATAATAATATATTATTTCACTACACTTATACATACAAACCTATAATAATATATTATTTCACTACACTTATACATACAAACCTCCC', 3))
"""