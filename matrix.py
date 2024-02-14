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

def matmul(M1, M2):
    if (len(M1) > 0 and len(M2) > 0):
        if (len(M2) == len(M1[0])):
            Mres = []
            