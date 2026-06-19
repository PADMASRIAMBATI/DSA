# num = [0,2,3,1]
# n = len(num)
# for i in range(n+1):
#     if i not in num:
#         print(i)

# print("---BRUTE FORCE--")
# num = [0,2,3,1,4,5,7,8]
# n = len(num)
# for i in range(n+1):
#     flag = 0
#     for j in range(n):
#         if num[j]==i:
#             flag=1
#             break
#     if flag ==0:
#         print(i)


# print("---BETTER FORCE(hasing)--")
# num = [0,2,3,1,4,5,7,6,8]
# n = len(num)
# hash = [0]*(n+1)
# for i in range(n+1):
#     if i in num:
#         hash[i] = 1
#     if hash[i]==0:
#         print(i)



# print("---OPTIMAL FORCE(sum)--")
# num = [2,3,1,4]
# n = len(num)
# sum = 0
# result = (n*(n+1))//2
# for i in range(n):
#     sum += num[i]
# result = result - sum
# print(result)



print("---OPTIMAL FORCE(XOR)--")
num = [1,3,6,4,5,0]
n = len(num)
xor1,xor2 = 0,0
for i in range(n+1):
    xor1 = xor1 ^ i
for j in num:
    xor2 = xor2 ^ j
print(xor1 ^ xor2)