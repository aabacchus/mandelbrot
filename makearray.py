from numba import njit
import numpy as np
nmax=50
@njit(fastmath=True)
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
    if c.real > -0.6 and c.real < 0.17:
        if c.imag < 0.4 and c.imag > -0.4:
            return nmax
    while abs(z) <= 2 and n < nmax:
        z = z*z+c
        n+=1
    return n
mbs=[]

@njit()
def loop(zoom):
    arra = []
    for a in range(-512,512+1,1):
        row = []
        for b in range(-360,360+1,1):
            c = complex(-np.e/7-np.e/20+a/(700+zoom),b/(700+zoom)+0.01)
            theM = mandelbrot(c)
#            if theM.real == 0:
#                continue
#            row.append([c,theM.real])
            row.append(theM.real)
        arra.append(row)
#    arrNp = np.array(arra)
    return arra

for i in range(50):
    arrNp = loop(100*i)
    np.save('mbsNp'+str(i).zfill(3),arrNp)
    print(i)
#print('saved data from {} to {} as mbsNp.npy'.format(-1500/1000,500/1000))
