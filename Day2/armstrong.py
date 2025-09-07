def armstrong(n):
    for i in range(1,n+1):
        x=i
        sum=0
        
        for j in range(len(str(i))):
            rem=x%10
            sum=sum+rem*rem*rem
            x=x//10
        if(i==sum):
            print(i,end=" ")
armstrong(1000)