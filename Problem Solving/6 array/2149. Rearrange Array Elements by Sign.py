print("---For equal number of positive and negative elements:---")
num = [3,1,-2,-5,2,-4]
n = len(num)
pos = []
neg = []
for i in range(n):
    if num[i] < 0:
        neg.append(num[i])
    if num[i] > 0:
        pos.append(num[i])
for i in range(n//2):
    num[i*2] = pos[i]
    num[i*2+1] = neg[i]
print(num)


num = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
n = len(num)
pos = 0
neg = 1
ans = [0]*n
for i in range(n):
    if num[i] > 0:
        ans[pos] = num[i] 
        pos += 2
    elif num[i] < 0:
        ans[neg] = num[i]
        neg += 2
print(ans)

print("---For unequal number of positive and negative elements:---")

num = [1,2,3,-4,-1,-2,-3,-5,-6]
n = len(num)
pos = []
neg = []
for i in range(n):
    if num[i] > 0:
        pos.append(num[i])
    elif num[i] < 0:
        neg.append(num[i])
if len(neg) < len(pos):
    for i in range(len(neg)):
        num[i*2] = pos[i]
        num[i*2+1] = neg[i]
    index = len(neg)*2
    for i in range(len(neg),len(pos)):
        num[index] = pos[i]
        index += 1
    
else:
    for i in range(len(pos)):
        num[i*2] = pos[i]
        num[i*2+1] = neg[i]
    index = len(pos)*2
    for i in range(len(pos),len(neg)):
        num[index] = neg[i]
        index += 1
print(num)
 