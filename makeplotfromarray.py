from numba import njit
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

@njit(fastmath=True)
def colorIn():
    x=[]
    y=[]
    colors=[]
    for jk in range(0,len(mbs)):
        re = mbs[jk][0].real
        im = mbs[jk][0].imag
        x.append(re)
        y.append(im)
        col=1-(nmax**0.5*mbs[jk][1].real**0.5/(nmax+1))
        colors.append(col)
    return x,y,colors
x,y,colors = colorIn()

print("done colors")

#for jk in range(0,len(mbs)):
#    re = mbs[jk][0].real
#    im = mbs[jk][0].imag
#    x.append(re)
#    y.append(im)
#    col=1-(nmax**0.5*mbs[jk][1]**0.5/(nmax+1))
#    colors.append((col,col,col))

#plt.scatter(x,y,marker=',',c=colors,s=1)
#plt.xlabel("real")
#plt.ylabel("imaginary")
#plt.title("n < "+str(nmax)+", 4.2M")
#plt.savefig('m03.png')
