l3=[]
freqcount={}
for i in range(1,7):
    print("Enter an element to append:")
    ele=int(input())
    l3.append(ele)
print(ele)
for i in l3:
    if i in freqcount:
        freqcount[i]+=1
    else:
        freqcount[i]=1
print(freqcount)
