from math import fabs
n=[-1,-3,-5,-6]
s=0
for i in range(len(n)):
    s+=fabs(n[i])
    print(s)
