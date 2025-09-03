#check whether the number is positive or negative
def NegOrpos(x):
    return x<0
a=int(input())
if NegOrpos(a):
    print(f'{a} is negative')
else:
    print(f'{a} is positive')