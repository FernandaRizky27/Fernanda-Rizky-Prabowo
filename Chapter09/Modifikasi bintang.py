def bintang(n):
    space=2*n-1
    for i in range(n):
        if(i<4):
         print(('*'*(2*i+1)).center(space))
        if(i>3):
         print(('*'*(13-(i)*2)).center(space))
bintang(7)