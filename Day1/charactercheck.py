def charactercheck(x):
    return x.isalpha()
a=input()
if charactercheck(a):
    print(f'{a} is an alphabet')
else:
     print(f'{a} is not an alphabet')