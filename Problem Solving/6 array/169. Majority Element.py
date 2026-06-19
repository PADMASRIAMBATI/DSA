num = [2,2,3,3,1,2,2]
n = len(num)
for i in range(n):
    count = 0
    for j in range(n):
        if num[i] == num[j]:
            count += 1
            
if count > (n/2):
    print(num[i])

# # num = [2,2,3,3,1,2,2]
# # n = len(num)
# # hashmap = {}
# # for i in num:
# #     if i in hashmap:
# #         hashmap[i] += 1
# #     else:
# #         hashmap[i] = 1

# # for i in hashmap:
# #     if hashmap[i] > (n/2):
# #         print(i)



# num = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
# n = len(num)
# element = 0
# count = 0
# for i in range(n):
#     if count == 0:
#         element = num[i]
#         count = 1
#         print(element)
#     elif element == num[i]:
#         count += 1
#     else: 
#         count -= 1
#     print(count)

# count1 = 0
# for i in range(n):
#     if num[i] == element:
#         count1 += 1
# if count1 > (n/2):
#     print(element)