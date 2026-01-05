n=37
k=5
c=0
for i in range(1,n+1,k):
    c+=1
    print(c,i)
n = 9
a = 2
c = 0
while n > a:
    n -= a
    c += 1
    if n <= a:
        print(c, n)
