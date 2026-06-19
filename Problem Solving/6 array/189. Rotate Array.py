# n = [1,2,3,4,5]
# temp = n[0]
# for i in range(1,len(n)):
#     n[i-1]=n[i]
# n[-1]=temp
# print(n)


# nums = [1,2,3,4,5,6,7]
# k = 3
# n = len(nums)
# rotated = []
# for i in range(n):
#     rotated.append(nums[(i+k)%n])
# print(rotated)


# nums = [1,2,3,4,5,6,7]
# l = 7
# n = len(nums)
# l = l % n
# temp = []
# for i in range(l):
#     temp.append(nums[i])
# for j in range(l,n):
#     nums[j-l]=nums[j]
# for k in range(len(temp)):
#     nums[n-l+k]=temp[k]
# print(nums)

# nums = [1,2,3,4,5,6,7]
# k = 2
# n = len(nums)
# k = k % n
# def reverse(nums,l,r):
#     r-=1
#     while l<r:
#         nums[l],nums[r]=nums[r],nums[l]
#         l+=1
#         r-=1
# print(nums)
# reverse(nums,0,k)
# print(nums)
# reverse(nums,k,n)
# print(nums)
# reverse(nums,0,n)
# print(nums)


# print("RIGHT ROTATE")
# nums = [1,2,3,4,5,6,7]
# d = 2
# n = len(nums)
# d = d%n
# temp = []
# for i in range(n-d,n):
#     temp.append(nums[i])
# for j in range(n-d-1,-1,-1):
#     nums[j+d]=nums[j]
# for k in range(len(temp)):
#     nums[k]=temp[k]
# print(nums)


print("RIGHT ROTATE")
nums = [1,2,3,4,5,6,7]
d = 2
n = len(nums)
d = d%n
def reverse(nums,l,r):
    r-=1
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
reverse(nums,0,n-d)
reverse(nums,n-d,n)
reverse(nums,0,n)
print(nums)




