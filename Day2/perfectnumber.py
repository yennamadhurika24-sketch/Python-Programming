def perfectNum(n):
    for i in range(1,n+1):
        x=i
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum=sum+j
        if(sum==i):
            print(sum,end=" ")
perfectNum(100)