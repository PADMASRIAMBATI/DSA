print('-----Brute Force-----')
n = 36
list = []
def is_prime(a):

    if a < 2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            return False
    return True
for i in range(2,n+1):
    if n%i == 0:
        if is_prime(i):
            list.append(i)
print(list)


print('-----Better Approach-----')
n = 780
list = []
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        if is_prime(i):
            list.append(i)
        if is_prime(n//i):
            list.append(n//i)
print(list)

print('-----Optimal Approach-----')
n = 780
list = []

for i in range(2,int(n**0.5)+1):
    while n%i == 0:
        n = n//i
        if i not in list:
            list.append(i)
print(list)

print('-----Print Prime Factors for Multiple Numbers-----')
arr = [2, 3, 4, 5, 6]
list = []
for n in arr:
    temp = []
    
    for i in range(2,int(n**0.5)+1):
        while n%i == 0:
            temp.append(i)
            n = n//i
    if n > 1:
        temp.append(n)
    list.append(temp)
print(list)
