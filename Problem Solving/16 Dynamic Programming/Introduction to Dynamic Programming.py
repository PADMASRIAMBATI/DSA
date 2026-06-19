print('-----Fibonacci Number in Recursion-----')
n = 10
def fun(index):
    if index <= 1:
        return index
    return fun(index-1) + fun(index-2)
print(fun(n))


print('-----Fibonacci Number in Dynamic Programming (Memoization)-----')
n = 10
dp = [-1]*(n+1)
def fun(index):
    if index <= 1:
        return index
    if dp[index] != -1:
        return dp[index]
    dp[index] = fun(index-1) + fun(index-2)
    return dp[index]
print(fun(n))


print('-----Fibonacci Number in Dynamic Programming (Tabulation)-----')
n = 10
dp = [-1]*(n+1)
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])


print('-----Fibonacci Number in Dynamic Programming (Tabulation) space optimization-----')
n = 10
prev2 = 0
prev = 1
for i in range(2,n+1):
    curr = prev + prev2
    prev2 = prev
    prev = curr
print(prev)