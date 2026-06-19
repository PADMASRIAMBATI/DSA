print("----Brute Force Approach----")
num = [2,6,5,8,11]
k = 14
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == k:
            print([i,j])

print("----Better Approach using Hashing----")
num = [2,6,5,8,11]
k = 14
hashmap = {}
for i in range(len(num)):
    value = k-num[i] 
    if value in hashmap:
        print([hashmap[value],i])
        break
    hashmap[num[i]] = i


print("----optimal Approach using 2 pointers----")
num = [2,5,8,11,6]
k = 14
l = 0
r = len(num)-1
flag = 0
num.sort()
while l<r:
    if num[l] + num[r] > k:
        r-=1
    elif num[l] + num[r] < k:
        l+=1
    else:
        flag = 1
        break
if flag == 1:
    print("YES")
else:
    print("NO")
    
