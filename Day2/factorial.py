def fact(n):
    
    while(n>1):
        print(n,end='*')
        n=n-1
    print(n)
n=int(input())
fact(n)