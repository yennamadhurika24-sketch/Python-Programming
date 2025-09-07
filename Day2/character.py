def characters(a):
    if a.isalpha():
        print(a," is an aplhabet")
    elif a.isdigit():
        print(a," is a digit")
    else:
        print(a," is a special character")
n=(input())
characters(n)