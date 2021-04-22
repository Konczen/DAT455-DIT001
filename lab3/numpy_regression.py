from numpy import *
import sys
import matplotlib.pyplot as plt

def powers(inpList,p1,p2):
	m1=[]
	for j in inpList:
		m2=[]
		for i in range(p1,p2+1):
			result=j**i
			m2.append(result)
		m1.append(m2)
	mat = array(m1)
	return mat

def poly(a, x):
    Y2 = a[0]
    for i in range(len(a)-1):
        Y2 = Y2 + a[i+1] * x ** (i+1)
    return Y2

f = loadtxt(sys.argv[1])  
f_2 = int(sys.argv[2])

data = transpose(f)
X = data[0]
Y = data[1]

Xp  = powers(X,0,f_2)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

Xmin = X[0]
Xmax = X[-1]

n = (round((abs(Xmin - Xmax))/0.2))

X2 = linspace(Xmin, Xmax, n).tolist()
X2 = array(X2)

Y2 = poly(a, X2)
    
plt.plot(X,Y,'ro')
plt.plot(X2,Y2)
plt.show()
