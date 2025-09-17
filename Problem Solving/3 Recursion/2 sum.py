# Parameter
def sum(n,result):
    if n < 1:
        print(result)
        return
    sum(n-1,result+n)
n = 3
sum(n,0)

print("---- Functional ------")
def sum_of_n(n):
    if n==0:
        return 0
    return n + sum_of_n(n-1)
n = 5
print(sum_of_n(n))