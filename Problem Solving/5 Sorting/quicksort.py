def quicksort(nums):
    low = 0
    high = len(nums)-1
    def quick(nums,low,high):
        if low < high:
            pivort_index = partition(nums,low,high)
            quick(nums,low,pivort_index-1)
            quick(nums,pivort_index+1,high)
        return nums
    def partition(nums,low,high):
        pivot = nums[low]
        i = low
        j = high
        while i < j:
            while i<=high and nums[i]<=pivot:
                i = i+1
            while j>=low and nums[j]>pivot:
                j = j-1
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[low], nums[j] = nums[j], nums[low]
        return j
    return quick(nums,low,high)

nums = [5, 6, 7, 8, 9, 0, 4, 3, 2, 1]
print(quicksort(nums))