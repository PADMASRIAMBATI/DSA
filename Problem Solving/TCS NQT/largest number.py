num = [8, 10, 5, 7, 9]
num1 = sorted(num)
print(num1[len(num)-1])

max = num[0]
for i in range(len(num)):
    if max < num[i]:
        max = num[i]
print(max)