# nums1 = [1,2,3,4,66]
# nums2 = [2,3,4,5,6,66]
# intersection = []
# n1 = len(nums1)
# n2 = len(nums2)
# for i in range(n1):
#     for j in range(n2):
#         if nums1[i] == nums2[j] and nums1[i] not in intersection:
#             intersection.append(nums1[i])
# print(intersection)


nums1 = [1,2,3,4,66,99,100]
nums2 = [2,3,4,5,6,66,99]
intersection = []
n1 = len(nums1)
n2 = len(nums2)
i,j = 0,0
while i<n1 and j<n2:
    if nums1[i] < nums2[j]:
        i+=1
    elif nums1[i] > nums2[j]:
        j+=1
    else:
        intersection.append(nums1[i])
        i+=1
        j+=1
print(intersection)