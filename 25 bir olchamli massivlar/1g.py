n=[1,5,3,4]
s=0
for i in range(len(n)-1):
    s-=n[i]+n[i+1]
    print(s)