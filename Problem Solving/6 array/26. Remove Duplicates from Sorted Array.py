# n = [1,1,2]
# k = sorted(set(n))
# for i in range(len(k)):
#     n[i] = k[i]
# print(k)

num = [3,1,1,2,3]
# temp = []
# nums=sorted(num)
# for  i in nums:
#     if not temp or temp[-1] != i:
#         temp.append(i)
# for j in range(len(temp)):
#     nums[j]=temp[j]
# print(nums)

i = 0
num.sort()
for j in range(len(num)):
    if num[i]!= num[j]:
        i+=1
        num[i]=num[j]
print(num)