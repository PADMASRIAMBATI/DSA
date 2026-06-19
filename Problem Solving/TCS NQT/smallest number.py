num = [8, 10, 5, 7, 9]
num1 = sorted(num)
print(num1[0])

min = num[0]
for i in range(len(num)):
    if min < num[i]:
        min = min
    else:
        min = num[i]
print(min)