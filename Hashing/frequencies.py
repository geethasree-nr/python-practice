class Solution:
    def countFrequencies(self, nums):
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        repeated=[]
        for key in d:
            repeated.append([key,d[key]])
        return repeated
nums=[1,2,2,1,3]
obj=Solution()
print(obj.countFrequencies(nums))