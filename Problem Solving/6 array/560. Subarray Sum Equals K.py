print('-----Brute Force-----')
num = [1,2,3,-3,1,1,1,4,2,-3]
num1 = [3,-3,1,1,1]
k = 3
n = len(num)
count = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += num[j]
        if sum == k:
            count += 1
print(count)


print('-----Better Approach-----')
num = [1,2,3,-3,1,1,1,4,2,-3]
count = 0
prefix_sum = 0
map = {0:1}
for i in num:
    prefix_sum += i

    if prefix_sum-k in map:
        count += map[prefix_sum-k]
    
    map[prefix_sum] = map.get(prefix_sum,0)+1

print(count)
