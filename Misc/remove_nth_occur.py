class new():
    def search(self,n):
        s=n[0].split()
        check=[]
        for i in s:
            if i not in check:
                check.append(i)
        print(check)

E=new()
n=["Every day is earth day"]  
E.search(n)
