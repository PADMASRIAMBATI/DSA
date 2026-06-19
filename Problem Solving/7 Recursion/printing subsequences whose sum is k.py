print('-----Print Possible ways-----')
num = [1,2,1]
k = 2
n = len(num)
ds = []
index = 0
sum = 0
def fun(index,ds,sum,n):
    if index == n:
        if sum == k:
            print(ds)
        return
    ds.append(num[index])
    fun(index+1,ds,sum+num[index],n)

    ds.pop()
    fun(index+1,ds,sum,n)
fun(index,ds,sum,n)

print('-----Print Only first output-----')
num = [1,2,1]
k = 2
n = len(num)
index = 0
sum = 0
ds = []
def fun(index,ds,sum,n):
    if index == n:
        if sum == k :
            print(ds)
            return True
        return False
    ds.append(num[index])
    if fun(index+1,ds,sum+num[index],n) == True:
        return True

    ds.pop()
    if fun(index+1,ds,sum,n) == True:
        return True
    return False
fun(index,ds,sum,n)


print('-----Print Count Only-----')
num = [1,2,1]
k = 2
n = len(num)
ds = []
index = 0
sum = 0
def fun(index,ds,sum,n):
    if index == n:
        if sum == k:
            return 1
        return 0
    ds.append(num[index])
    left = fun(index+1,ds,sum+num[index],n)
    ds.pop()
    right = fun(index+1,ds,sum,n)
    return left + right
print(fun(index,ds,sum,n))