# n=[2,1,3,4,5,6,12,44,54,76]
# b=12
# index=0
# for i in range(len(n)):
#     if n[i]>b:
#         index+=i
#         print(index,n[i])
#         break

n=[1,4,3,2,5]
b=4
index=0
masssive=[]
for i in range(len(n)):
    if n[i]>b:
     masssive.append(n[i])
print(min(masssive))
for j in range(len(n)):
    if min(masssive)==n[j]:
        index=j
        print(f' 1 dan katta bulgan eng katta son {min(masssive)} va uning index raqami {index}')
    else:
        print(0)