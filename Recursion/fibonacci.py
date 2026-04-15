class Solution:
    def fib(self, n):
        first_num=0
        sec_num=1
        for i in range(n):
            temp=first_num + sec_num
            first_num=sec_num
            sec_num=temp
        return first_num
        
n=6
obj=Solution()
print(obj.fib(n))