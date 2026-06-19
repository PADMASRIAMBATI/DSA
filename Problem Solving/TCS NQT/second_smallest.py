num = [1, 2, 4, 7, 7, 5]  
num1 = sorted(num)
print("Second Smallest :",num1[1])
print("Second Largest :",num1[len(num)-2])

print("second largest")
secl = float('-inf')
larg = float('-inf')
for i in range(len(num)):
    if num[i] > larg:
        secl = larg
        larg = num[i]
    elif num[i] < larg and num[i] > secl:
        secl = num[i]
print(secl)

print("second small")
secs = float('inf')
small = float('inf')
for i in range(len(num)):
    if num[i] < small:
        secs = small
        small = num[i]
    elif num[i] > small and num[i] < secs:
        secs = num[i]
print(secs)