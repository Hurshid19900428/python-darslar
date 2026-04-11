# n=[2,3,6,5]
# s=0
# for i in range(len(n)):
#     s+=n[i]**2
#     print(s)

n=(int(input('n = ')))
s=0
a=[]
for i in range(n):
    a.append(int(input('i = ')))
print(a)
for j in range(len(a)):
    s+=a[j]**2
    print(s)