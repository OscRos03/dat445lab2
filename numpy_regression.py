import sys 
from numpy import *
import matplotlib.pyplot as plt

def powers(M, n1, n2):
    Mp = []
    for i in range(len(M)):
        Mp.append([])
        for j in range(n1, n2+1):
            Mp[i].append(M[i]**j)
    return array(Mp)

Min_temp=10
Max_temp=30
Data=loadtxt("chirps.txt")

Transposed_data=transpose(Data)

X=Transposed_data[0]
Y=Transposed_data[1]

Xp = powers(X,0,1)
Yp = powers(Y,1,1)
Xptransposed = transpose(Xp)

[[b],[m]] = matmul(linalg.inv(matmul(Xptransposed,Xp)),matmul(Xptransposed,Yp))

Y2=[b+m*x for x in X]

for x in range(Min_temp,Max_temp+1):
    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)

plt.show()