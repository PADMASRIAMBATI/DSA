print("-----Brute Force Approach-----")
num = [1,2,3,4,5,6,4]
n = len(num)
for i in range(n):
    if (i == 0 or num[i-1] < num[i]) and (i == n-1 or num[i] > num[i+1]):
        print(num[i])

print("-----Optimal Approach-----")
num = [1,2,3,4,5,6,4]
n = len(num)
if n == 1:
    print(num[0])
elif num[0] > num[1]:
    print(num[0])
elif num[n-1] > num[n-2]:
    print(num[n-1])
low = 1
high = n-2
while low <= high:
    mid = (low+high)//2
    if num[mid-1] < num[mid] > num[mid+1]:
        print(num[mid]) 
        break
    elif num[mid-1] < num[mid] < num[mid+1]:
        low = mid+1
    else:
        high = mid-1

print("-----Optimal Approach (For multiple peak's)-----")
num = [1,2,3,4,5,6,4]
n = len(num)
if n == 1:
    print(num[0])
elif num[0] > num[1]:
    print(num[0])
elif num[n-1] > num[n-2]:
    print(num[n-1])
low = 1
high = n-2
while low <= high:
    mid = (low+high)//2
    if num[mid-1] < num[mid] > num[mid+1]:
        print(num[mid])
        break
    elif num[mid-1] < num[mid] < num[mid+1]:
        low = mid + 1
    else:
        high = mid - 1
