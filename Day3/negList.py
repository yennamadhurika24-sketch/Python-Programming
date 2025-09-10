negList=[]
for i in range(5):
    print("enter an element:")
    ele=int(input())
    if(ele<0):
        negList+=[ele]
    else:
        pass
    #negList.append(i)
print(negList)