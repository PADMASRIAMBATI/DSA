arr = [3, 2, 1, 5, 2, 10, 10 , 99]
result = arr[0]
for i in range(len(arr)):
    if arr[i]> result:
           result = arr[i]
print(result)