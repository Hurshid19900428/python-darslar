n=8
f_1=f_2=1
f_i=0
for i in range(3,n+1):
    f_i=f_2+f_1
    f_1=f_2
    f_2=f_i
    print(f_i)