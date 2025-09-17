def bubble_sort(nums):
    n = len(nums)
    def bubble(nums,n):
        if n==1:
            return nums
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1] , nums[i]
        return bubble(nums,n-1)
    return bubble(nums,n)
nums = [10, 8, 92, 65, 44, 86]
print(bubble_sort(nums))