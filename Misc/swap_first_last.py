class change():
    def swaps(self,n):
        m=len(n)
        for i in n:
            n[0],n[m-1]=n[m-1],n[0]
        print(n)
c=change()
n=[12,35,9,56,24]
print(n)
c.swaps(n)
