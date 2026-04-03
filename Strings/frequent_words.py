def freq_words():
    s=input("Enter a string:").lower()
    d={}
    for i in s :
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    for i in  d:
            print(i,"Occurs",d[i],'Times')
    
    
freq_words()
    
    
str=input("Enter a string:").lower()
s=set(str)
for i in s:
    print(i ,"=",str.count(i),"times")
