def naturalSum(n):
    i=1
    sum=0
    while(i<=n):
        sum=sum+i
        i=i+1
    return sum
n=int(input())
print("Sum=",naturalSum(n))