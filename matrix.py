def transpose(M):
    Mt = []
    if len(M) > 0:
        for i in range(len(M[0])):
            Mt.append([])

    for column in range(len(M)):
        for row in range(len(M[column])):
            Mt[row].append(M[column][row])
    return Mt

def powers(M, n1, n2):
    Mp = []
    for i in range(len(M)):
        Mp.append([])
        for j in range(n1, n2+1):
            Mp[i].append(M[i]**j)
    return Mp