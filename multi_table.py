def multiplication_table(size):
    #for all numbers in range 1 to size+1
    rowIdx = 2
    # numIdx = 0
    matrix = []
    rowOne = [i for i in range(1, size+1)]
    matrix.append(rowOne)
    while rowIdx <= size:
        row = [num * rowIdx for num in rowOne]
        matrix.append(row)
        rowIdx += 1
    return matrix
print(multiplication_table(3))
        
