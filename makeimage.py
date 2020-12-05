from PIL import Image
import numpy as np
from numba import njit
@njit()
def makeA(x):
    w,h = x.shape
    maxX = x.max()
    print(maxX)
    t=(h,w,3)
    A=np.zeros(t,dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            A[i,j]=[x[j][i]/maxX*255]*3
    #print('made array')
    return A

for im in range(50):
    A=makeA(np.load('images/mbsNp'+str(im).zfill(3)+'.npy'))

    i=Image.fromarray(A,"RGB")
    #print('made image,saving')
    #i.show()
    i.save('images/mbsNp'+str(im).zfill(3)+'.png',"PNG")
    print(im)
