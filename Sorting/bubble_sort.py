nums=[1,10,11,5,2]
while True:
    a=True
    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            a=False
    if a==True:
        break


print(nums)