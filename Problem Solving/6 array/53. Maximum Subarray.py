# num = [5,4,-1,7,8]
# n = len(num)
# max_sum = 0
# for i in range(n):
#     sum = 0
#     for j in range(i,n):
#         sum += num[j]
#         max_sum = max(sum,max_sum)
# print(max_sum)

num = [-2,-3,4-1,-2,1,5,-3]
n = len(num)
max_sum = num[0]
sum = 0
for i in range(n):
    sum += num[i]
    if sum > max_sum:
        max_sum = sum
    if sum < 0:
        sum = 0
print(max_sum)

num = [-2,-3,4-1,-2,1,5,-3]
n = len(num)
max_sum = num[0]
sum = 0
start = 0
ans_start = -1
ans_end = -1
for i in range(n):
    sum += num[i]
    if sum > max_sum:
        max_sum = sum
        ans_start = start
        ans_end = i
    if sum < 0:
        sum = 0
        start = i + 1
print(max_sum,[ans_start,ans_end])