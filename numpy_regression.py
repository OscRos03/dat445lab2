import sys 
from numpy import *
import matplotlib.pyplot as plt

def powers(M, n1, n2):
    Mp = []
    for i in range(len(M)):
        Mp.append([])
        for j in range(n1, n2+1):
            Mp[i].append(M[i]**j)
    return Mp

def powers2(M, n1, n2):
    Mp=array([])
    for i in range(len(M)):
        append([])
        for j in range(n1, n2+1):
            Mp[i].append(M[i]**j)
    return Mp

Min_temp=10
Max_temp=30
#Data=loadtxt(sys.argv[1])
Data=loadtxt("chirps.txt")

Transposed_data=transpose(Data)




X=Transposed_data[0]
Y=Transposed_data[1]

X_float=[float(x) for x in X]
Y_float=[float(x) for x in Y]

Xp  = powers2(X_float,0,1)
Yp  = powers2(Y_float,1,1)
Xptransposed = transpose(Xp)

[[b],[m]] = matmul(linalg.inv(matmul(Xptransposed,Xp)),matmul(Xptransposed,Yp))

Y2=[b+m*x for x in X_float]





for x in range(Min_temp,Max_temp+1):
    plt.plot(X_float,Y_float,'ro')
    plt.plot(X_float,Y2)


plt.show()
