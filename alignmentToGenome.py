import sys, collections, math, random
import numpy as np

def localAlignment(hom_area, string, gap):
    # Create an alignment matrix initialized with zeros
    matrix = makeMatrix(len(hom_area), len(string))

    high_score = 0
    opt_loc = (0,0)

    # Walk through the grid and fill in
    for i in range(1, len(hom_area)):
        for j in range(1, len(string)):
            # recurrant definition of the matrix
            matrix[i][j] = max(
                matrix[i][j-1] + gap,
                matrix[i-1][j] + gap,
                matrix[i-1][j-1] + similarityMatrix(hom_area[i], string[j]),
                0
            )

            # Keep track of the cell with largest score
            if matrix[i][j] >= high_score:
                high_score = matrix[i][j]
                opt_loc = (i,j)
    
    return high_score, opt_loc, matrix

def makeMatrix(x, y):
    # function that creates matrix
    return [[0] * y for i in range(x)]

def symbolToNumber(symbol):
        """
        Helper function for pattern_to_number
        """
        if symbol == "A":
            return 0
        elif symbol == "C":
            return 1
        elif symbol == "G":
            return 2
        elif symbol == "T":
            return 3
        else:
            raise ValueError("Invalid Symbol in string!")

def similarityMatrix(symb1, symb2):
    # Function that returns similarity between two symbols 
    num1 = symbolToNumber(symb1)
    num2 = symbolToNumber(symb2)

    similarity_matrix = [[10, -1, -3, -4], [-1, 7, -5, -3], [-3, -5, 9, 0], [-4, -3, 0, 8]]

    return similarity_matrix[num1][num2]

def retrace(matrix, opt_loc, hom_area, string, gap):
    i = opt_loc[0]
    j = opt_loc[1]
    string1 = ''
    string2 = ''
    
    # While the scor of the matrix is larger than 0 we continue backtracking
    while i >= 0 and j >= 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + similarityMatrix(hom_area[i], string[j]):
            string1 = hom_area[i] + string1
            string2 = string[j] + string2
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i-1][j] + gap:
            string1 = hom_area[i] + string1
            string2 = '-' + string2
            i -= 1
        else:
            string1 = '-' + string1
            string2 = string[j] + string2
            j -= 1
    
    return string1, string2


"""
stringA = 'ACTACAATATTCGA'

stringB = 'ATCGCAATT'

result_local_alignment = localAlignment(stringA, stringB, -10)

results = retrace(result_local_alignment[2], result_local_alignment[1], stringA, stringB, -10)

print(results[0])
print(results[1])
"""