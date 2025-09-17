def insertion_sort(nums):
    n = len(nums)
    def insertion(nums,n):
        if n <= 1:
            return
        insertion(nums,n-1)
        j = n-1
        while j > 0 and nums[j-1]>nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j = j-1
    insertion(nums,n)
    return nums

nums = [22, 77, 11, 99, 66, 1, 0, 43]
print(insertion_sort(nums))