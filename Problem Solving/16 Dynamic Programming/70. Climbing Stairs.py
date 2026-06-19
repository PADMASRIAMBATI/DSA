n = 2
def fun(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    left = fun(n-1)
    right = fun(n-2)
    return left+right
print(fun(n))

