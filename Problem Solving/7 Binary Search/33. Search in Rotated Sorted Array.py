nums = [4,5,6,7,0,1,2]
target = 0
low = 0
high = len(nums)-1
while low <= high :
    mid = (low+high) // 2
    if nums[mid] == target:
        print(mid)
    if nums[low] <= nums[mid]:
        if nums[low] <= target <= nums[mid]:
            high = mid-1
        else:
            low = mid+1
    elif nums[high] >= nums[mid]:
        if nums[mid] <= target <= nums[high]:
            low = mid+1
        else:
            high = mid -1

