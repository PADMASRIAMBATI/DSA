print('-----Brute Force-----')
matrix = [[1,2,3],[4,5,6],[7,8,9]]
r = len(matrix)
c = len(matrix[0])
ans = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        ans[j][r-i-1] = matrix[i][j]
print(ans)

print('-----Optimal Approch-----')
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
r = len(matrix)
c = len(matrix[0])
for i in range(r):
    for j in range(i+1,c):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for i in range(r):
    matrix[i].reverse()
print(matrix)