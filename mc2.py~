import matplotlib.pyplot as plt
nmax=50
def mandelbrot(c):
    z=0
    n=0
    if c.real < -0.75:
        if c.imag > 0.45 or c.imag < -0.5:
            return 0
    if c.real < -0.3:
        if c.imag > 0.7 or c.imag < -0.7:
            return 0
    if c.real > 0.1:
        if c.imag > 0.7 or c.imag < -0.7:
            return 0
    while abs(z) <= 2 and n < nmax:
        z = z*z+c
        n+=1
    return n
mbs=[]
for a in range(-15000,5000+1,1):
    print(a)
    for b in range(-10500,10500+1,1):
        c = complex(-0.019+a/10000,b/10000+0.0)
        mbs.append([c,mandelbrot(c)])
#print(mbs)

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
plt.title("n < "+str(nmax))
plt.legend()
plt.show()
#for a in range(-74900,-74400-1,1):
#    print(a)
#    for b in range(11000,11500,1):
#        c = complex(a/100000,b/100000)
