# 1752
#Brute Force Approach
print("-----Brute Force Approch-----")

arr = [3,4,5,1,2,7]
n = len(arr)
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
found = False
for x in range(n):
    rotated = []
    for i in range(n):
        rotated.append(arr[(i+x)%n])
    if is_sorted(rotated):
        found = True
        break
print(found)
# or
def check(nums):
    n = len(nums)
    for x in range(n):
        rotated = [nums[(i+x)%n] for i in range(n)]
        if all(rotated[i] >= rotated[i+1] for i in range(n-1)):
            return True
    return False
print(check(arr))


#Optimal Approach
print("-----Optimal Approach-----")

n = len(arr)
count = 0
for j in range(n):
    if arr[j] < arr[j-1]:
        count+=1

if count <= 1:
    print(True)
else:
    print(False)
print(count)
