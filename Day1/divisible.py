#check whether the number is divisible by 5 and 11 or not
def divisible(x):
    if( x%5==0 and x%11==0):
        print(x,' is divisible by 5 and 11')
    else:
        print(x,' is not divisible by 5 and 11')
a=int(input())
divisible(a)