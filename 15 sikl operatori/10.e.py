from math import sqrt

n=6
a=3
s=1
for i in range(2,n+1):
    s*=sqrt(a*(i-1))**i
    print(s)