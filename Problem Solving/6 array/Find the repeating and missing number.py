print('-----Brute Force-----')
nums = [4,3,6,2,1,1]
n = len(nums)
missing = -1
repeated = -1
for i in range(1,n+1):
    count = 0
    for j in range(n):
        if nums[j] == i:
            count += 1
    if count == 2:
        repeated = i
    elif count ==0:
        missing = i
    if repeated != -1 and missing != -1:
        break
        
print([repeated,missing])

print("-----Better Approach-----")
num = [4,3,6,2,1,1]
n = len(num)
hash = [0]*(n+1)
repeated = -1
missing = -1
for i in num:
    hash[i] += 1
for j in range(1,n+1):
    if hash[j] == 2:
        repeated = j
    elif hash[j] == 0:
        missing = j
    if repeated != -1 and missing != -1:
        break
print([repeated,missing])

print('-----1st Optimal Solution(Using Maths)-----')
num = [4,3,6,2,1,1]
n = len(num)
# for x-y
x = 0 #sum of array elements
y = (n*(n+1)) // 2  # sum of n natural numbers
# for x square - y square
x1 = 0 # square of sum of array elements
y1 = (n*(n+1)*((2*n) + 1)) // 6

for i in range(n):
    x += num[i]
    x1 += num[i] * num[i]

value1 = x-y
value2 = x1-y1
value2 = value2 // value1
x = (value1 + value2) // 2
y = value2 - x
print([x,y])


print('-----2nd Optimal Solution(Using XOR)-----')
num = [4,3,6,2,1,1]
n = len(num)
xor = 0
for i in range(n):
    xor = xor ^ num[i] ^ (i+1)
bitno = 0
while 1:
    if(xor & (1<<bitno) != 0):
        break
    bitno += 1
zero = 0
one = 0
for i in range(n):
    # 1's club
    if (num[i] & (1<<bitno)) != 0:
        one = one^num[i]
    # 0's club
    else:
        zero = zero^num[i]
for i in range(1,n+1):
    if (i & (1<<bitno)) != 0:
        one = one ^ i
    else:
        zero = zero ^ i
count = 0
for i in range(n):
    if num[i] == zero:
        count += 1
if count == 2:
    print([zero,one])
else:
    print([one,zero])