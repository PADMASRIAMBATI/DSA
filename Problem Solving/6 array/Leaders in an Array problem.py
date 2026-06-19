num1 = [1,2,5,3,1,2]
num = [-3,4,5,1,-4,-5]

print("----Brute force----")
ans = []
n = len(num)
for i in range(n):
    leader = True
    for j in range(i+1,n):
        if num[i] < num[j]:
            leader = False
            break
    if leader==True:
        ans.append(num[i])
print(ans)


print("----Optimal Approch----")
n = len(num)
ans = []
last_num = num[-1]
ans.append(last_num)
for i in range(n-2,-1,-1):
    if num[i] > last_num:
        ans.append(num[i])
        last_num = num[i]
ans.reverse()
print(ans)