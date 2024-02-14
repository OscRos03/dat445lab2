import sys 
from matrix import *
import matplotlib.pyplot as plt

Min_temp=10
Max_temp=30
Data=loadtxt(sys.argv[1])
#Data=loadtxt("chirps.txt")

Transposed_data=transpose(Data)




X=Transposed_data[0]
Y=Transposed_data[1]

X_float=[float(x) for x in X]
Y_float=[float(x) for x in Y]

Xp  = powers(X_float,0,1)
Yp  = powers(Y_float,1,1)
Xptransposed = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xptransposed,Xp)),matmul(Xptransposed,Yp))

Y2=[b+m*x for x in X_float]





for x in range(Min_temp,Max_temp+1):
    plt.plot(X_float,Y_float,'ro')
    plt.plot(X_float,Y2)


plt.show()
