l2=[3,6,8,1,9]
print("enter an element to delete:")
x=int(input())

if x in l2:
    idx=l2.index(x)
    l3=l2[:idx]+l2[idx+1:]
print(l3)