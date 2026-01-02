from math import sqrt
def tenglama(a,b,c):
    while True:
        D = sqrt(4*a*b*c)
        if D>0:
            print(D)
            break
        else:
            print('bu manfiy qayta son kiriting : ')
tenglama(1,-2,3)
