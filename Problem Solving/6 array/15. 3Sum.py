print('-----Brute Force-----')
num = [-1,0,1,2,-1,-4]
ans = set()
n = len(num)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if i != j != k:
                if (num[i] + num[j] + num[k]) == 0:
                    triplet = tuple(sorted([num[i],num[j],num[k]]))
                    ans.add(triplet)
res = [list(i) for i in ans]
print(res)

print('-----Better Approach-----')
num = [-1,0,1,2,-1,-4]
n = len(num)
ans = set()
for i in range(n):
    hash = set()
    for j in range(i+1,n):
        third = -(num[i] + num[j])
        if third in hash:
            ans.add(tuple(sorted([num[i],num[j],third])))
        hash.add(num[j])
result = [list(i) for i in ans]
print(result)


print('-----Optimal Approach-----')
num = [-1,2,2,-1,-2,-2,2,-2,-1,0,0,2,0]
n = len(num)
num.sort()
ans = []
for i in range(n):
    if i>0 and num[i] == num[i-1]:
        continue
    j = i+1
    k = n-1
    while j < k:
        s = num[i]+num[j]+num[k]
        if s == 0:
            ans.append([num[i],num[j],num[k]])
            j += 1
            k -= 1
            while num[j] == num[j-1] and j<k:
                j += 1
            while num[k] == num[k+1] and j<k:
                k -= 1
        elif s < 0:
            j += 1
        else:
            k -= 1
print(ans)

