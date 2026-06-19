print('-----Recursion-----')
i = 3
j = 7
def fun(i,j):
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    up = fun(i-1,j)
    left = fun(i,j-1)
    return up + left
print(fun(i-1,j-1))

print('-----Memoization-----')
i = 3
j = 7
dp = [[-1]*(j) for _ in range(i)]
def fun(i,j):
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = fun(i-1,j) + fun(i,j-1)
    return dp[i][j]
print(fun(i-1,j-1))

print('-----tabulation-----')
m = 3
n = 7
dp = [[-1]*n for _ in range(m)]
dp[0][0] = 1
for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if i > 0:
            up = dp[i-1][j]
        else: 
            up = 0
        if j > 0:
            left = dp[i][j-1]
        else:
            left = 0
        dp[i][j] = up + left
print(dp[m-1][n-1])
