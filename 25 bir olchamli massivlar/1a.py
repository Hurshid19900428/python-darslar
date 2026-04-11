n=int(input('n = '))
a=[]
s=0

for i in range(n):
    a.append(int(input('i = ')))
print(a)
for j in range(len(a)):
    s+=a[j]
    print(s)