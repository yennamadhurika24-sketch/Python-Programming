def sumOfDigits(n):
    sum=0
    rem=0
    while(n>0):
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input("Enter n="))
print("Sum of digits of a number=",(sumOfDigits(n)))