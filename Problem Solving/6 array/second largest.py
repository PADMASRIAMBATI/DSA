# Brute force approach
print("Brute Force Approch")
arr = [1, 2, 4, 7, 7, 5]
arr.sort()
result = arr[len(arr)-1]
secondl = -1
for i in range(len(arr)-1,-1,-1):
    if arr[i] != result:
        secondl = arr[i]
        break
print(secondl)

# Better approach
print("Better Approch")
largest = arr[0]
for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
second_largest = -1
for j in range(len(arr)):
    if arr[j]>second_largest and arr[j]!=largest:
        second_largest = arr[j]
print(second_largest)


# Optimal approach
print("Optimal Approch")

larg = arr[0]
sec_larg = -1
for i in range(len(arr)):
    if arr[i]>larg:
        sec_larg = larg
        larg = arr[i]
    elif arr[i]<larg and arr[i]>sec_larg:
        sec_larg = arr[i]
print(sec_larg)