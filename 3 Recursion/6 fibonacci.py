def fibonacci(n):
    if n <= 1:
        return n
    last = fibonacci(n-1)
    sec_last = fibonacci(n-2)
    return last + sec_last
n = 7
print(fibonacci(n))