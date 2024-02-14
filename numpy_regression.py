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

def poly(a,x):
    q=0
    for index in range(0,len(a)):
        q+= a[index]*(x**index)
    return q
    
Min_temp=10
Max_temp=30

Data=loadtxt(sys.argv[1])
n=int(sys.argv[2])

Transposed_data=transpose(Data)
X=Transposed_data[0]
Y=Transposed_data[1]

Xp  = powers(X,0,n)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

X_low=float(X[0])
X_high=float(X[-1])
step_size=int((X_high-X_low)/0.2)

X2=linspace(X_low,X_high,step_size).tolist()

Y2=[poly(a, x) for x in X2]

for x in range(Min_temp,Max_temp+1):
    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)

plt.show()