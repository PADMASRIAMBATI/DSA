print("---BRUTE FORCE (using linear search)---")
num = [11, 11, 4, 4, 5, 85, 23, 85, 23]
n = len(num)
for i in range(n):
    
    a = num[i]
    count = 0
    for j in range(n):
        if num[j]==a:
            count +=1
    if count == 1:
        print(a)

print("---BETTER APPROCH (using dictonary)---")
num = [11, 11, 4, 4, 5, 85, 23, 85, 23]
n = len(num)
map = {}
for i in num:
    if i in map:
        map[i] += 1
    else:
        map[i] = 1
for key in map:
    if map[key] == 1:
        print(key)


print("---OPTIMAL APPROCH (using XOR)---")
num = [11, 11, 4, 4, 5, 85, 23, 85, 23]
n = len(num)
xor =0
for i in range(n):
    xor = xor ^ num[i]
print(xor)