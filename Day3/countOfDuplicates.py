def countOfduplicates(l1):
    c=0
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    duplicates=len(l1)-len(l2)
    return l2,duplicates
l1=[1,2,3,3,5,6,8,5,8,2]
a,b=countOfduplicates(l1)
print("List without duplicates=",a)
print("count of duplicate elements=",b)