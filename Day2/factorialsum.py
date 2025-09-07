def factorialsum(a):
    
    for i in range(1,a+1):
        n=i
        sum=0
        
        while(n>0):
            rem=n%10
            fact=1
            for k in range(1,rem+1):
                fact*=k
            sum+=fact
            n=n//10
        if(sum==i):
            print(sum,end=" ")
       
factorialsum(200)
            