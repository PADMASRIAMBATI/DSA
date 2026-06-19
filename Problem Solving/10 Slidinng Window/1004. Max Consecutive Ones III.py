print('-----Brute Force-----')
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
n = len(nums)
max_length = 0
for i in range(n):
    zero = 0
    for j in range(i,n):
        if nums[j] == 0:
            zero += 1
        if zero <= k:
            max_length = max(max_length,j-i+1)
        else:
            break
print(max_length)

print('-----Optimal Approach-----')
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
n = len(nums)
l = 0
max_length = 0
zeros = 0
for r in range(n):
    if nums[r] == 0:
        zeros += 1
        
    while zeros > k:
        if nums[l] == 0:
            zeros -= 1
        l += 1
    max_length = max(max_length,r-l+1)
print(max_length)