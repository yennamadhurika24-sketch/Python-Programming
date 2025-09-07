def sumOfFirstLastdigit(n):
    l=n%10
    rem=0
    while n>0:
        rem=n%10
        n=n//10
    return l+rem

print(sumOfFirstLastdigit(234))