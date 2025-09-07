def palindrome(n):
    for i in range(1,n+1):
        y=str(i)
        z=y[::-1]
        
        if(y==z):
            print(i,end=" ")
palindrome(150)