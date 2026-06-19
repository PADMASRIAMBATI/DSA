# a = [1,2,3,4,2,4,5,6]
# b = [2,3,5,6,7,8]
# union = []
# for i in range(len(a)):
#     if a[i] not in union:
#         union.append(a[i])
# for i in range(len(b)):
#     if b[i] not in union:
#         union.append(b[i])
# print(union)


# a = [1,2,3,4,2,4,5,6]
# b = [2,3,5,6,7,8]
# union = []
# for i in range(len(a)):
#     union.append(a[i])
# for i in range(len(b)):
#     union.append(b[i])
# print(set(union))

#Only two sorted arrays
nums1 = [1,1,2,3,4,5,7,54,3,5,1,1,76]
nums2 = [2,3,4,4,5,6,100,1000,100]
union =[]
l,r = 0,0
n1 = len(nums1)
n2 = len(nums2)
while l<n1 and r<n2:
    if nums1[l]>nums2[r]:
        if nums2[r] not in union:
            union.append(nums2[r])
        r+=1
    elif nums1[l]<nums2[r]:
        if nums1[l] not in union:
            union.append(nums1[l])
        l+=1
    else: # nums1[l] == nums2[r]
        if nums1[l] not in union:
            union.append(nums1[l])
        l+=1
        r+=1
while l<n1:
    if nums1[l] not in union:
        union.append(nums1[l])
    l+=1
while r<n2:
    if nums2[r] not in union:
        union.append(nums2[r])
    r+=1
print(union)