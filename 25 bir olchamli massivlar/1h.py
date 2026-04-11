from math import factorial
n=[1,5,3,4]
c=0
s=0
for i in range(len(n)-1):
    c+=1
    s+=n[i]/factorial(c)-n[i+1]/factorial(c+1)
    print(s)



