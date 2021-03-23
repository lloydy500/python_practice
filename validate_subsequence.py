def isValidSubsequence(array, sequence):
    # Write your code here.
    arridx = 0
    seqidx = 0
    # for i in array:
    #     for num in sequence:
	# 		if num == i:
    #             sqidx += 1
    #         arridx += 1
    # return arridx == seqidx
    while arridx < len(array) and seqidx < len(sequence):
        if array[arridx] == sequence[seqidx]:
            seqidx += 1
        arridx += 1
    return seqidx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(isValidSubsequence(array, sequence))