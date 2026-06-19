num = [1,2,3,1,1,1,1,4,2,3]
l = 10
n = len(num)
max_length = 0
for i in range(n):
    for j in range(i,n):
        sum = 0
        for k in range(i,j):
            sum += num[k]
        if sum == l:
            max_length = max(max_length,j-i)
print(max_length)


num = [1,2,3,1,1,1,1,4,2,3]
l = 10
n = len(num)
max_length = 0
for i in range(n):
    sum = 0 
    for j in range(i,n):
        sum += num[j]
        if sum == l:
            max_length = max(max_length,j-i+1)
print(max_length)


num = [1,2,3,1,1,1,1,4,2,3]
l = 10
prefix_sum = 0
hash = {}
max_length = 0
for i in range(len(num)):
    prefix_sum += num[i]
    if prefix_sum == l:
        max_length = max(max_length,i+1)
    if (prefix_sum-l) in hash:
        max_length = max(max_length,i-hash[prefix_sum-l])
    if prefix_sum not in hash:
        hash[prefix_sum] = i
print(max_length)


num = [1,2,3,1,1,1,1,3,3]
l = 10
sum = 0
i = 0
max_length = 0
for j in range(len(num)):
    sum += num[j]
    while sum > l:
        sum -= num[i]
        i+=1
    if sum == l:
        max_length = max(max_length,j-i+1)
print(max_length)