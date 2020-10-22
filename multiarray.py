import matplotlib.pyplot as plt
from multiprocessing import Process
import math

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
    if c.real > -0.6 and c.real < 0.17:
        if c.imag < 0.4 and c.imag > -0.4:
            return nmax
    while abs(z) <= 2 and n < nmax:
        z = z*z+c
        n+=1
    return n
mbs=[]

nums=[]
for a in range(-150,50+1,1):
    print(a)
    for b in range(-105,105+1,1):
        c = complex(-0.019+a/100,b/100+0.0)
        nums.append(c)
            
#for num in nums:
#    mbs.append([num,mandelbrot(num)]

def gen_mbs(num,arr):
    arr.append([num,mandelbrot(num)])

nums1=nums[:math.floor(len(nums)/800)-1]
nums2=nums[math.floor(len(nums)/3)-1:math.floor(len(nums)*2/3)-1]
nums3=nums[math.floor(len(nums)*2/3)-1:]

if __name__ == '__main__':
        processes=[]
        for num in nums1:
            proc=Process(target=gen_mbs, args=(num,mbs))
            processes.append(proc)
            print(proc)
            proc.start()
        for p in processes:
            p.join()
        print(mbs)
#plt.scatter(x,y,marker=',',c=colors,s=1)
#plt.xlabel("real")
#plt.ylabel("imaginary")
#plt.title("n < "+str(nmax)+", 4.2M")
#plt.legend()
#plt.savefig('m00.svg')
#for a in range(-74900,-74400-1,1):
#    print(a)
#    for b in range(11000,11500,1):
#        c = complex(a/100000,b/100000)
