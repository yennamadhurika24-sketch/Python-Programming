def leapyr(x):
    if((x%4==0 and x%100!=0) or (x%100==0 and x%400==0)):
        print(f'{x} is a leap year')
    else:
        print(f'{x} is not a leap year')
a=int(input())
leapyr(a)