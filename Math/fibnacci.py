class fibo:
    def demo(self,n):
        first_num=0
        sec_num=1
        print(first_num,end=" ")
        print(sec_num,end=" ")
        for i in range(n):
            third_num=first_num + sec_num
            first_num=sec_num
            sec_num=third_num
            print(third_num,end=" ")
f=fibo()
n=int(input("Enter the Number:"))
f.demo(n)
