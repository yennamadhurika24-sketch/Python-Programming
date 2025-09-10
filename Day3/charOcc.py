def CharOcc(x,str1):
    for i in range(len(str1)):
        if str1[i]==x:
            print(i,end=" ")
str1="HappyBirthday"
CharOcc('a',str1)