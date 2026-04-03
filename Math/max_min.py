class maxmin():
    def maxi_mini(self,n):
        maxi_num=n[0]
        mini_num=n[0]
        for i in n:
            if i > maxi_num:
                maxi_num=i
                print(f"Max num in {n} is = {maxi_num}")
            if i < mini_num:
                mini_num=i
                print(f"Min num in {n} is = {mini_num}")

m=maxmin()
n=[20,10,40]
m.maxi_mini(n)


