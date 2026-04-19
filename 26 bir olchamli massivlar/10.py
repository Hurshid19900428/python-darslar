
n=[1,2,3,4,5,6,7]
juft =[]
toq=[]
n=sorted(n)
for i in n:
    if i%2==0:
        juft.append(i)
for i in n:
    if i%2!=0:
        toq.append(i)
print(juft+toq[::-1])












