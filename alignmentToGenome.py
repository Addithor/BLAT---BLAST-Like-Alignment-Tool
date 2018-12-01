import collections

def localAlignment(hom_area, string, gap):
    # Create an alignment matrix initialized with zeros
    matrix = makeMatrix(len(hom_area) + 1, len(string) + 1)

    high_score = 0
    opt_loc = (0,0)
    
    for i in range(1, len(hom_area) + 1):
        matrix[i][0] = gap * i
    
    for j in range(1, len(string) + 1):
        matrix[0][j] = gap * j
    

    # Walk through the grid and fill in
    for i in range(1, len(hom_area) + 1):
        for j in range(1, len(string) + 1):
            # recurrant definition of the matrix
            matrix[i][j] = max(
                matrix[i][j-1] + gap,
                matrix[i-1][j] + gap,
                matrix[i-1][j-1] + similarityMatrix(hom_area[i-1], string[j-1]),
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
        # Changes symbol to number
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

    similarity_matrix = [[1, -3, -3, -3], [-3, 1, -3, -3], [-3, -3, 1, -3], [-3, -3, -3, 1]]

    return similarity_matrix[num1][num2]

def retrace(matrix, opt_loc, hom_area, string, gap, loc_hom_area):
    i = opt_loc[0]
    j = opt_loc[1]
    string1 = ''
    string2 = ''
    """
    print(opt_loc[0], opt_loc[1])

    for x in matrix:
        print(x)
    """
    # While i and j are larger or equal to 0 we continue retracing
    while not(i <= 0 or j <= 0):
        if matrix[i][j] == matrix[i-1][j-1] + similarityMatrix(hom_area[i-1], string[j-1]):
            string1 = hom_area[i-1] + string1
            string2 = string[j-1] + string2
            i -= 1
            j -= 1   
        elif matrix[i][j] == matrix[i-1][j] + gap:
            string1 = hom_area[i] + string1
            string2 = '-' + string2
            i -= 1          
        elif matrix[i][j] == matrix[i][j-1] + gap:
            string1 = '-' + string1
            string2 = string[j] + string2
            j -= 1   
        else:
            break

    # Where the alignment begins         
    new_opt_loc = loc_hom_area + i

    return string1, string2, new_opt_loc

