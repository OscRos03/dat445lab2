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
        if (len(M1[0]) == len (M2)):
            Mres = []
            for column1 in range(len(M1)):
                for row2 in range(len(M2[0])):
                    for column2 in range(len(M2)):
                        if not (0 <= column1 < len(Mres)):
                            Mres.append([])
                        if not (0 <= row2 < len(Mres[column1])):
                            Mres[column1].append(0)
                        Mres[column1][row2] += M1[column1][column2] * M2[column2][row2]
            return Mres
    return []

def invert(M):
    # hardcode gaming
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    Mres = [
                [M[1][1]/det,      M[0][1]/det*-1],
                [M[1][0]/det*-1,   M[0][0]/det],
            ]
    return Mres

# ork
def loadtxt(filename):
    file=open(filename,"r")
    l = [ line.split() for line in file]
   
    file.close()

    return l
