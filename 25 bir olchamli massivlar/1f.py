n=[1,2,3,4]
p=1
s=0
for i in range(len(n)):
    p*=n[i]
    s+=n[i]
    print(p,s)