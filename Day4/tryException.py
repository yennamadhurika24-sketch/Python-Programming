def division(a,b):
    c=a/b
    return c

try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print("c= ",division(a,b))
except:
    print("error:Division by zero is not allowed")
else:
    print("Divided succesfully!!")
finally:
    print("Iam in final block")