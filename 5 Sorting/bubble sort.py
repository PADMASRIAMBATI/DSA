def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr
arr = [13, 46, 24, 52, 20, 9]
print(bubble_sort(arr))


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr
arr = [13, 46, 24, 52, 20, 9]
print(bubble_sort(arr))