l1=[]
even=0
odd=0
for i in range(1,11):
    l1.append(i)
    if(i%2==0):
        even+=1
    else:
        odd+=1
print('list= ',l1)
print('even count=',even)
print('odd count= ',odd)