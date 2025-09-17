import sys

arr = [10, 20, 30]
print(sys.getsizeof(arr))  # size of list object itself
print(sys.getsizeof(arr[0]))  # size of first element (int object)
print(sys.getsizeof(arr[1]))  # size of second element (int object)