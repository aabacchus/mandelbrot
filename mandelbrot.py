import numpy
import matplotlib.pyplot as plt
z = [0]
mandelbrot = []

for a in numpy.linspace(-2.0,1.0,121):
    for b in numpy.linspace(-2,2,121):
        c = complex(round(a,2),round(b,2))
        z=[0]
        for x in range(0,50):
            if abs(z[x]) >2:
                n=x
                break
            z.append((z[x]**2)+c)
        #print(z)
        if abs(z[len(z)-1]) < 20:
            mandelbrot.append([c,n])

print(mandelbrot)
x=[]
y=[]
for jk in range(0,len(mandelbrot)):
    re = mandelbrot[jk][0].real
    im = mandelbrot[jk][0].imag
    x.append(re)
    y.append(im)
print(x)
plt.scatter(x,y,marker=',',color="green",s=1)
plt.xlabel("real")
plt.ylabel("imaginary")
plt.legend()
plt.show()
