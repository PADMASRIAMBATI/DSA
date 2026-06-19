# print('----First type of Question(given R and C find element)-----')
# row = 5
# colum = 3
# def nCr(row,colum):
#     n = row
#     r = colum
#     res = 1
#     for i in range(r):
#         res = res * (n-i)
#         res = res // (i+1)
#     return res
# print(nCr(row,colum))


# print('----To print a particular row elements-----')
# row = 5
# def nCr(row,colum):
#     n = row
#     r = colum
#     res = 1
#     for i in range(r):
#         res = res * (n-i)
#         res = res // (i+1)
#     return res
# for colum in range(row+1):
#     print(nCr(row,colum),end = " ")
# print()

# print('----((2nd method) To print a particular row elements-----')
# row = 6
# ans = 1
# print(ans,end=' ')
# for col in range(1,row):
#     ans = ans * ((row-col)) // col
#     print(ans,end=" ")
# print()


print('-----For all elements to be print-----')
numrows = 6
ans = []
def nCr(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res
for i in range(numrows):
    temp = []
    for j in range(i+1):
        temp.append(nCr(i,j))
    ans.append(temp)
print(ans)

print('-----(2nd method) For all elements to be print-----')
numrows = 6
ans = []
def rowlist(numrows):
    temp = []
    res = 1
    temp.append(res)
    for col in range(1,numrows):
        res = res * (numrows-col) // col
        temp.append(res)
    return temp
for i in range(1,numrows+1):
    ans.append(rowlist(i))

print(ans)