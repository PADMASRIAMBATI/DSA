print('-----Brute Force-----')
num = [15, -2, 2, -8, 1, 7, 10, 23]
n = len(num)
k = 0
max_length = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += num[j]
        if sum == k:
            max_length = max(max_length,j-i+1)
print(max_length)

print('-----Better Approach-----')
num = [15, -2, 2, -8, 1, 7, 10, 23]
n = len(num)
k = 0
max_length = 0
prefix_sum = 0
hash = {}
for i in range(n):
    prefix_sum += num[i]
    if prefix_sum == k:
        max_length = max(max_length,i+1)
    if (prefix_sum-k) in hash:
        max_length = max(max_length,i-hash[prefix_sum-k])
    if prefix_sum not in hash:
        hash[prefix_sum] = i
print(max_length)


print('-----Optimal Approach-----')
num = [15, -2, 2, -8, 1, 7, 10, 23]
n = len(num)
k = 0
i = 0
sum = 0
max_length = 0
for j in range(n):
    sum += num[j]
    while sum > k:
        sum -= num[i]
        i += 1
    if sum == k:
        max_length = max(max_length,j+1-i)
print(max_length)