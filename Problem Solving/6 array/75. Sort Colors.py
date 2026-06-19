# num = [0,1,2,0,1,2,1,2,2,2,2,2,0,0,0,1]
# n = len(num)
# count0 = 0
# count1 = 0
# count2 = 0
# for i in range(n):
#     if num[i] == 0:
#         count0 += 1
#     elif num[i] == 1:
#         count1 += 1
#     elif num[i] == 2:
#         count2 += 1
# for i in range(count0):
#     num[i] = 0
# for j in range(count0,count1+count0):
#     num[j] = 1
# for k in range(count1+count0,n):
#     num[k] = 2
# print(num)


num = [0,1,1,0,1,2,1,2,0,0,0]
low = 0
mid = 0
high = len(num)-1
while mid <= high:
    if num[mid] == 0:
        num[low], num[mid] = num[mid],num[low]
        mid += 1
        low += 1
    elif num[mid] == 1:
        mid += 1
    else:
        num[mid], num[high] = num[high],num[mid]
        high -= 1
print(num)