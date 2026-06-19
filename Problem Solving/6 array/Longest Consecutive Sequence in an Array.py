num1 = [0,3,7,2,5,8,4,6,0,1]
num = [102,4,100,1,101,3,2,1,1]

print("-----Brute Force-----")
n = len(num)
large = 0 
def LinearSearch(num,a):
    for i in range(len(num)):
        if num[i] == a:
            return True
    return False
for i in range(n):
    x = num[i]
    count = 1
    while (LinearSearch(num,x+1) == True):
        count += 1
        x += 1
    large = max(large,count)
print(large)

num = [102,4,100,1,101,3,2,1,1]
print("-----Better Approch-----")
n = len(num)
num.sort()
large = 0
count = 0
last_small = float('-inf')
for i in range(n):
    if num[i] == last_small:
        continue
    elif num[i] == last_small+1:
        count += 1
        last_small = num[i]
    else:
        count = 1
        last_small = num[i]
    large = max(large,count)
print(large)


num = [102,4,100,1,101,3,2,1,1]
print("-----Optimal Approch-----")
n = len(num)
large = 0
num_set = set(num)
for i in num_set:
    if i-1 not in num_set:
        count = 1
        x = i
        while x+1 in num_set:
            count += 1
            x = x + 1
    large = max(large,count)
print(large)