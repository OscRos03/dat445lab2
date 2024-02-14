import sys 
from matrix import *
import matplotlib.pyplot as plt

Min_temp=10
Max_temp=30
Data=loadtxt(sys.argv[1])

Transposed_data=transpose(Data)

X=Transposed_data[0]
Y=Transposed_data[1]

Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xptransposed = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xptransposed,Xp)),matmul(Xptransposed,Yp))

Y2=[b+m*x for x in X]

for x in range(Min_temp,Max_temp+1):
    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)

plt.show()
