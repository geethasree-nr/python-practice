class Solution:
    def mostFrequentElement(self, nums):
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        max_freq=0
        result=-1
        for i in d:
            if d[i]>max_freq:
                max_freq=d[i]
                result=i
        return result
nums=[1, 2, 2, 3, 3, 3]
obj=Solution()
print(obj.mostFrequentElement(nums))