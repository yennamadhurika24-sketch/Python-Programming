def noofDigits(a):
    c=0
    while(a>0):
     
        c=c+1
        a=a//10
    return c
print(noofDigits(234))