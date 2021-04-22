from matrix import *
import sys
import matplotlib.pyplot as plt


f = loadtxt(sys.argv[1])
data = transpose(f)
X = data[0]
Y = data[1]
Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    
Y2 = []
for i in X:
    p_chirps = b + m * i
    Y2.append(p_chirps)

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()
    
