def pattern2(n):
    for i in range(1,n):
        for j in range(1,n):
            if(i==j or i==n-j):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
n=int(input("Enter n:"))
pattern2(n)