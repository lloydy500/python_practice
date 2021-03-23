def data_reverse(data):
    no_of_bytes = int(len(data) / 8)
    a = []
    for i in range(no_of_bytes):
        b = data[:8]
        print(b)
        a.append(b)
        del data[:8]
    return sum(a[::-1], [])
data1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]

print(data_reverse(data1))
