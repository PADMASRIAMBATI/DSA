nums = [14,9,15,12,6,8,13]
n = len(nums)
for i in range(n):
    j = i
    while(j>0 and nums[j-1]>nums[j]):
        nums[j] , nums[j-1] = nums[j-1], nums[j]
        j = j-1
print(nums)