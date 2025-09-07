def prime(n):
    i=1
    c=0
    while(i<=n):
        if(n%i==0):
            c=c+1
        i=i+1
    if(c==2):
        return True
    else:
        return False
def primefactors(a):
    for i in range(1,a+1):
        if a%i==0 and prime(i):
            print(i,end=" ")
primefactors(10)
            
        