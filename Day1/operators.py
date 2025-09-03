def add(a,b):
    return a+b
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c

def div(a,b):
    c=a/b
    return c
def mod(a,b):
    c=a%b
    return c
x=int(input())
y=int(input())

print("Addition=",add(x,y))


print("Subtraction=",sub(x,y))


print("Multiplicat=",mul(x,y))
print("Division=",div(x,y))
print("Modulus division=",mod(x,y))