def occurances(str2):
    freq={}
    str1=""
    for i in range(len(str2)):
        if str2[i] in freq:
            freq[str2[i]]+=1
        else:
            freq[str2[i]]=1
    for i in freq:
    
        str1+=i+str(freq[i])
    print(str1)
str2="madhurika"
occurances(str2)