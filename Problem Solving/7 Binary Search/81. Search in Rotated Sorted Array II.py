num = [3,1,2,3,3,3,3]
target = 3
low = 0
high = len(num)-1
found = False
while low <= high:
    mid = (low+high)//2
    if num[mid] == target:
        found = True
    if num[mid] == num[low] == num[high]:
        low = low+1
        high = high-1
        continue
    if num[low] <= num[mid]:
        if num[low] <= target <= num[mid]:
            high = mid-1
        else:
            low = mid+1
    else:
        if num[mid] <= num[high]:
            if num[mid] <= target <= num[high]:
                low = mid+1
            else:
                high = mid-1
print(found)