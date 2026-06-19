# # print('-----Brute Force-----')
# # nums1 = [1,2,3] 
# # m = 3
# # nums2 = [2,5,6]
# # n = 3
# # left = 0
# # right = 0
# # temp = []
# # while left < m and right < n:
# #     if nums1[left] <= nums2[right]:
# #         temp.append(nums1[left])
# #         left += 1
# #     else:
# #         temp.append(nums2[right])
# #         right += 1
# # while left < m:
# #     temp.append(nums1[left])
# #     left += 1
# # while right < n:
# #     temp.append(nums2[right])
# #     right += 1
# # for i in range(m+n):
# #     if i < m:
# #         nums1[i] = temp[i]
# #     else:
# #         nums2[i-m] = temp[i]
# # print(nums1)
# # print(nums2)

# # print('-----Better Approach-----')
# # nums1 = [1,3,5,7] 
# # nums2 = [0,2,6,8,9]
# # m = len(nums1)
# # n = len(nums2)
# # i = m-1
# # j = 0
# # while i >= 0 and j < n:
# #     if nums1[i] > nums2[j]:
# #         nums1[i], nums2[j] = nums2[j], nums1[i]
# #         i-=1
# #         j+=1
# #     else:
# #         break
# # nums1.sort()
# # nums2.sort()
# # print(nums1,nums2)


# print('-----Gap Method-----')
# arr1 = [1,3,5,7] 
# arr2 = [0,2,6,8,9]
# n = len(arr1)
# m = len(arr2)
# length = n+m
# gap = (length//2)+(length%2)
# def swap(num1,num2,index1,index2):
#     if num1[index1] > num2[index2]:
#         num1[index1], num2[index2] = num2[index2], num1[index1]
# while gap > 0:
#     left = 0
#     right = gap
#     while right < length:
#         # arr1 and arr2
#         if left < n and right >= n:
#             swap(arr1,arr2,left,right-n)
#         # arr2 and arr
#         elif left >= n:
#             swap(arr2,arr2,left-n,right-n)
#         # arr1 and arr1
#         else:
#             swap(arr1,arr1,left,right)
#         left += 1
#         right += 1
#     if gap <= 1:
#         break
#     gap = (gap//2)+(gap%2)
# print(arr1)
# print(arr2)




arr1 = [1,3,4,5,7] 
arr2 = [0,2,6,8,9]
n = len(arr1)
m = len(arr2)
length = m+n
gap = (length//2)+(length%2)
def swap(num1,num2,index1,index2):
    if num1[index1] > num2[index2]:
        num1[index1], num2[index2] = num2[index2], num1[index1]
while gap > 0:
    left = 0
    right = gap
    while right < length:
        # arr1 and arr2
        if left < n  and right >= n:
            swap(arr1,arr2,left,right-n)
        # arr2 and arr2
        elif left >= n:
            swap(arr2,arr2,left-n,right-n)
        # arr1 and arr1
        else:
            swap(arr1,arr1,left,right)
        left += 1
        right += 1
    if gap == 1:
        break
    gap = (gap//2)+(gap%2)
print(arr1,arr2)