n=int(input('n = '))
p=1
a=[]
for i in range(n):
    a.append(int(input('i = ')))
print(a)
for j in range(len(a)):
    p*=a[j]
    print(p)

