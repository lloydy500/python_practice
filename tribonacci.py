def tribonacci(signature, n):
    
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n ==2:
        return [signature[0], signature[1]]

    arrIdx = 0
    newA = signature
    while arrIdx <= n - 4:
        nextNum = newA[arrIdx] + newA[arrIdx+1] + newA[arrIdx+2]
        newA.append(nextNum)
        arrIdx += 1
    return newA


print(tribonacci([1, 1, 1], 10))
