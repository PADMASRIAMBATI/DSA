print('-----Brute Force-----')
num = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
n = len(num)
num.sort()
i = 0
ans = []
while i < n:
    start = num[i][0]
    end = num[i][1]

    j = i+1
    while j < n and end >= num[j][0]:
        end = max(end,num[j][1])
        j += 1
    
    ans.append([start,end])
    i = j
print(ans)

print('-----Optimal Approach-----')
num = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]  
n = len(num)
num.sort()
ans = []
for i in num:
    if not ans or ans[-1][1] < i[0]:
        ans.append(i)
    else:
        ans[-1][1] = max(ans[-1][1],i[1])
print(ans)