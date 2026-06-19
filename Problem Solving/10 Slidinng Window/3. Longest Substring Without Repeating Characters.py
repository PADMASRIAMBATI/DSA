# print('-----Brute Force-----')
# s = 'cadbzabcd'
# n = len(s)
# max_len = 0
# for i in range(n):
# #     sum = ''
# #     for j in range(i,n):
# #         if s[j] in sum:
# #             break
# #         sum += s[j]
# #         len = j-i+1
# #         max_len = max(max_len,len)
# # print(max_len)


# print('-----Better Approach-----')
# s = 'cadbzabcd'
# n = len(s)
# max_length = 0
# for i in range(n):
#     hash = [0]*256
#     for j in range(i,n):
#         if hash[ord(s[j])] == 1:
#             break
#         length = j-i+1
#         max_length = max(length,max_length)
#         hash[ord(s[j])] = 1
# print(max_length)

print('-----Optimal Approach-----')
s = 'cadbzabcd'
n = len(s)
l = 0
max_length = 0
hash = {}
for r in range(n):
    if s[r] in hash and hash[s[r]] >= l:
        l = hash[s[r]]+1
    hash[s[r]] = r
    max_length = max(max_length,r-l+1)
    

print(max_length)

