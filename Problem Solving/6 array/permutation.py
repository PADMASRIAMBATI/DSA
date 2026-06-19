# num = [1,2,3]
# n = len(num)
# ds = []
# ans = []
# freq = [False]*n
# def permutation(num,ds,ans,freq):
#     if len(num) == len(ds):
#         ans.append(ds.copy())
#         return
#     for i in range(n):
#         if not freq[i]:
#             freq[i] = True
#             ds.append(num[i])
#             permutation(num,ds,ans,freq)
#             ds.pop()
#             freq[i] = False
# permutation(num,ds,ans,freq)
# print(ans)


num = [1,2,3]
n = len(num)
index = 0
ans = []
def permutation(index,num,ans):
    if len(num) == index:
        ans.append(num.copy())
        return
    for i in range(index,len(num)):
        num[i], num[index] = num[index], num[i]
        permutation(index+1,num,ans)
        num[i], num[index] = num[index], num[i]
permutation(index,num,ans)
print(ans)