from numba import jit
import numpy as np
#import ast
import matplotlib.pyplot as plt
nmax=50

#f = open('mbs.txt','r')
#mbs = ast.literal_eval(f.read())
#f.close()
x=[]
y=[]
colors=[]

mbs = np.load('mbs.npy')

print(mbs[0][1].real)
@jit(nopython=True)
def colorIn(c):
    col=1-(nmax**0.5*c**0.5/(nmax+1))
    return col

for jk in range(0,len(mbs)):
    re = mbs[jk][0].real
    im = mbs[jk][0].imag
    x.append(re)
    y.append(im)
    colors.append(colorIn(mbs[jk][1]).real)

print("done colors")

#for jk in range(0,len(mbs)):
#    re = mbs[jk][0].real
#    im = mbs[jk][0].imag
#    x.append(re)
#    y.append(im)
#    col=1-(nmax**0.5*mbs[jk][1]**0.5/(nmax+1))
#    colors.append((col,col,col))

plt.scatter(x,y,marker=',',c=colors,s=1)
plt.xlabel("real")
plt.ylabel("imaginary")
plt.title("n < "+str(nmax)+", 4.2M")
plt.savefig('m02.png')
