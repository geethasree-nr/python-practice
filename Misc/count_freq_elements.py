li=[15,15,12,6,7,10,12,20,10,28,10]
d={}
for i in li:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d:
    if d[i]>1:
        print(i,"occurs",d[i],"Times")
