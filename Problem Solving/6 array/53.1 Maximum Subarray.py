print("-----Brute Force-----")
arr = [-2,-3,4,-1,-2,1,5,-3]
max_sum = float('-inf')
n = len(arr)
for i in range(n):
    for j in range(i,n):
        curr_sum = 0 
        for k in range(i,j+1):
            curr_sum += arr[k]
        max_sum = max(curr_sum,max_sum)
print(max_sum)


print("-----Better-----")
arr = [-2,-3,4,-1,-2,1,5,-3]
max_sum = float('-inf')
n = len(arr)
for i in range(n):
    curr_sum = 0 
    for j in range(i,n):
        curr_sum += arr[j]
        max_sum = max(curr_sum,max_sum)
print(max_sum)


print("-----Optimal(Kadane's Algorithm)-----")
arr = [-2,-3,4,-1,-2,1,5,-3]
n = len(arr)
curr_sum = 0
max_sum = float('-inf')
for i in range(n):
    curr_sum += arr[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < 0:
        curr_sum = 0
    
print(max_sum)