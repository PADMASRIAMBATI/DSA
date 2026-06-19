# # print('-----Brute Force-----')
# # num = [1,0,-1,0,-2,2]
# # target = 0
# # ans = set()
# # n = len(num)
# # for i in range(n):
# #     for j in range(i+1,n):
# #         for k in range(j+1,n):
# #             for l in range(k+1,n):
# #                 if num[i]+num[j]+num[k]+num[l] == target:
# #                     quadruplets = tuple(sorted([num[i],num[j],num[k],num[l]]))
# #                     ans.add(quadruplets)
# # result = [list(i) for i in ans]
# # print(result)

# print('-----Better Approach-----')
# num = [1,0,-1,0,-2,2]
# num.sort()
# n = len(num)
# target = 0
# ans = set()
# for i in range(n):
#     for j in range(i+1,n):
#         hash = set()
#         for k in range(j+1,n):
#             s = target - (num[i]+num[j]+num[k])
#             if s in hash:
#                 ans.add((num[i],num[j],s,num[k]))
#             hash.add(num[k])
# result = [list(i) for i in ans]
# print(result)



print('-----Optimal Approach-----')
num = [5,4,4,1,5,2,3,2,4,1,2,3,1,3]
target = 8
num.sort()
n = len(num)
ans = []
for i in range(n):
    for j in range(i+1,n):
        if i > 0 and num[i] == num[i-1]:
            continue
        if j > i+1 and num[j] == num[j-1]:
            continue
        k = j+1
        l = n-1
        while k < l:
            s = num[i]+num[j]+num[k]+num[l]
            if s == target:
                ans.append([num[i],num[j],num[k],num[l]])
                k += 1
                l -= 1
                while k < l and num[k] == num[k-1]:
                    k += 1
                while k < l and num[l] == num[l+1]:
                    l -= 1
            elif s < target:
                k += 1
            else:
                l -= 1
print(ans)

