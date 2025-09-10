def VowelConsonants(str):
    c=0
    v=0
    
    for i in str:
        if i in ['a','e','i','o','u']:
            v+=1
        else:
            c+=1
       
    print("number of vowels=",v)
    print("Number of consonants=",c)
   
str=input("Enter a string").lower()
VowelConsonants(str)