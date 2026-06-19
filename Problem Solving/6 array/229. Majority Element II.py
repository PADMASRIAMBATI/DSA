print('-----Brute Force-----')
num = [1,1,1,3,3,2,2,2]
n = len(num)
ans = []
for i in range(n):
    if len(ans)== 0 or ans[0] != num[i]:
        count = 0
        for j in range(n):
            if num[i] == num[j]:
                count += 1
        if count > (n//3):
            ans.append(num[i])
    if len(ans) == 2:
        break
print(ans)

print('-----Better Approach-----')
num = [2,1,1,3,1,4,5,6]
n = len(num)
ans = [] 
hash = {}
majority = (n//3)+1
for i in range(n):
    hash[num[i]] = hash.get(num[i],0)+1
    if hash[num[i]] == majority:
        ans.append(num[i])
print(ans)


print('-----Optimal Approach-----')
num = [2,1,1,3,1,4,5,6]
n = len(num)
ans = []
count1, count2 = 0,0
element1, element2 = 0,0
for i in range(n):
    if count1 == 0 and num[i] != element2:
        count1 = 1
        element1 = num[i]
    elif count2 == 0 and num[i] != element1:
        count2 = 1
        element2 = num[i]
    elif num[i] == element1:
        count1 += 1
    elif num[i] == element2:
        count2 += 1
    else:
        count1 -= 1
        count2 -= 1
countA = 0
countB = 0
for i in range(n):
    if num[i] == element1:
        countA += 1
    elif num[i] == element2:
        countB += 1
if countA > (n//3):
    ans.append(element1)
if countB > (n//3):
    ans.append(element2)
print(ans)