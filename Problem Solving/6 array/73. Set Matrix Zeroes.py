print('-----Brute Force-----')
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
r = len(matrix)
c = len(matrix[0])
def MarkRow(i):
    for j in range(c):
        if matrix[i][j] != 0:
            matrix[i][j] = '@'
def MarkColum(j):
    for i in range(r):
        if matrix[i][j] != 0:
            matrix[i][j] = '@'
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 0:
            MarkRow(i)
            MarkColum(j)
for i in range(r):
    for j in range(c):
        if matrix[i][j] == '@':
            matrix[i][j] = 0
print(matrix)


print('-----Better Approch-----')
matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
r = len(matrix)
c = len(matrix[0])
row = [0]*r
colum = [0]*c
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 0:
            row[i] = 1
            colum[j] = 1
for i in range(r):
    for j in range(c):
        if row[i] == 1 or colum[j] == 1:
            matrix[i][j] = 0

print(matrix)


print('-----Better Approch-----')
matrix1 = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
matrix = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
matrix1 = [[0,1,2,0],[0,4,5,2],[1,3,1,5]]
r = len(matrix)
c = len(matrix[0])
col0 = 1
for i in range(r):
    if matrix[i][0] == 0:
        col0 = 0
    for j in range(1,c):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0

for i in range(1,r):
    for j in range(1,c):
        if matrix[i][j] != 0:
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
if matrix[0][0] == 0:
    for j in range(c):
        matrix[0][j] = 0
if col0 == 0:
    for i in range(r):
        matrix[i][0] = 0
print(matrix)
