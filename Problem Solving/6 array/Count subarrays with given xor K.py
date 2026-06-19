print('-----Brute Force-----')
num = [4, 2, 2, 6, 4]
k = 6
n = len(num)
count = 0
for i in range(n):
    xor = 0
    for j in range(i,n):
        xor ^= num[j]
        if xor == k:
            count += 1
print(count)

print('-----Optimal Approach-----')
num = [4, 2, 2, 6, 4]
k = 6
n = len(num)
xor = 0
count = 0
hash = {0:1}
for i in range(n):
    xor ^= num[i]
    if xor == k:
        count += 1
    if xor^k in hash:
        count += hash[xor^k]
print(count)
    