def kebabize(string):
    s_split =  [l for l in string]
    new_a = []
    for i, j in enumerate(s_split):
        print(j)
        if j.isnumeric():
            pass
        elif (j == j.upper()) and not new_a:
            new_a.append(j.lower())
        elif (j == j.upper()) and (i > 0):
            new_a.append('-')
            new_a.append(j.lower())
        else:
            new_a.append(j)
        print(new_a)
    return "".join(new_a)


print(kebabize('42'))
print(kebabize('1DOEOXKxm0u7DtQccfDKdpszORHGEtsbBUj9HQcu'))
