print("------ Using two pointers -------")
def reverse_array(arr,l,r):
    if l >= r:
        return
    arr[l] , arr[r] = arr[r], arr[l]
    reverse_array(arr,l+1,r-1)
arr = [1, 2, 3, 4]
print(arr)
reverse_array(arr,0,len(arr)-1)
print(arr)

print("------ Using single pointers -------")
def reverse_array1(a,i):
    n = len(a)
    if i >= n//2:
        return
    a[i] , a[n-i-1] = a[n-i-1] , a[i]
    reverse_array1(a,i+1)
a = [0, 1, 2, 3, 4, 5]
print(a)
reverse_array1(a,0)
print(a)

print("---------------------------")
def reverse(arr1,n):
    i = len(arr1)
    if n <= i//2:
        return
    arr1[i-n], arr1[n-1] = arr1[n-1], arr1[i-n]
    reverse(arr1,n-1)
arr1 = [1, 2, 3, 4, 5]
reverse(arr1,len(arr1))
print(arr1)
