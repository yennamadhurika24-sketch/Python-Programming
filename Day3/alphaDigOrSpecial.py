def alphaDigSpecialCharcCount(str):
    a=0
    d=0
    s=0
    for i in str:
        if i.isalpha():
            a+=1
           
        elif i.isdigit():
            d+=1
            
        else:
            s+=1
            
    print("Number of characters=",a)
    print("number of digits=",d)
    print("Number of special characters=",s)
str=input("enter a string=")
alphaDigSpecialCharcCount(str)
