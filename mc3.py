import ast
import matplotlib.pyplot as plt
nmax=50

f = open('mbs.txt','r')
mbs = ast.literal_eval(f.read())

x=[]
y=[]
colors=[]
for jk in range(0,len(mbs)):
    re = mbs[jk][0].real
    im = mbs[jk][0].imag
    x.append(re)
    y.append(im)
    col=1-(nmax**0.5*mbs[jk][1]**0.5/(nmax+1))
    colors.append((col,col,col))

plt.scatter(x,y,marker=',',c=colors,s=1)
plt.xlabel("real")
plt.ylabel("imaginary")
plt.title("n < "+str(nmax)+", 4.2M")
plt.legend()
plt.savefig('m02.png')
