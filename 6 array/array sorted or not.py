nums = [ 3,4,2,1,2]
def sort(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True

print(sort(nums))

def sorted(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            count += 1
    if nums[-1] > nums[0]:
        count += 1
    return count <= 1
print(sorted(nums))

def sorted1(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            return False
        return True
print(sorted1(nums))

# n=5
# for i in range(2,7):
#     print(f"{i} % {n} = {i%n}")