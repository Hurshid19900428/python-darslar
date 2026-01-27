n=[2,1,3,4,5,6,12,45,44,54,76]
index=0
a=3
c=54
temp=[]
for i in range(len(n)):
    if a<n[i]<c:
        temp.append(n[i])
        index=i
print(max(temp),index)


#
# n = [2, 4, 3, 8, 7, 6, 9]
# b = 4
# c = 6
# indexb=0
# indexc=0
# sub=0
# massiv=[]
# for i in range(len(n)):
#     if b==n[i]:
#         indexb+=i
#     elif c==n[i]:
#         indexc+=i
#         print(indexb,indexc)
# for j in range(len(n)):
#     if indexb<j<indexc:
#         massiv.append(n[j])
# print(max(massiv))