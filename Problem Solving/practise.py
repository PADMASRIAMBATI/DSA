# nums = [3,3]
# target = 6
# n = len(nums)
# for i in range(n):
#     for j in range(i+1,n): 
#         if nums[i] + nums[j] == target:
#             print([i,j])

# hashmap = {}
# for i in range(n):
#     sum = target - nums[i]
#     if sum in hashmap:
#         print([hashmap[sum],i])
#     hashmap[nums[i]]=i

# nums = [2,2,1,1,1,2,2]
# count = 0
# element = 0
# n = len(nums)
# for i in range(n):
#     if count == 0:
#         element = nums[i]
#         count += 1
#     elif element == nums[i]:
#         count += 1
#     else:
#         count -= 1
# count1 = 0
# for i in range(n):
#     if nums[i] == element:
#         count1 += 1
# if count1 > (n/2):
#     print(element)


# nums = [2,2,1,1,1,2,2]
# n =len(nums)
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if nums[i] == nums[j]:
#             count+= 1
# if count > (n/2):
#     print(nums[i])

# nums = [2,2,1,1,1,2,2]
# n =len(nums)
# hash = {}
# for i in nums:
#     if i in hash:
#         hash[i] += 1
#     else:
#         hash[i] = i
# for key in hash:
#     if hash[key] > (n/2):
#         print(key)
# print(hash)

# nums = [7,6,4,3,1]
# n = len(nums)
# for i in range(n):
#     for j in range(i,n):
#         if nums[i] < nums[j]:
            

# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     break_point = int((2*i+1)/2)
#     char = ord("A")
#     for j in range(2*i+1):
#         print(chr(char),end=" ")
#         if j < break_point:
#             char += 1
#         else:
#             char -= 1
#     for j in range(n-i+1):
#         print(" ",end=" ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(2*i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(2*(n-i-1)):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(2*(n-i-1)):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n-1):
#     for j in range(n-i-1):
#         print("*",end=" ")
#     for j in range(2*(i+1)):
#         print(" ",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()

# n = 3
# char = ord("A")
# for i in range(n):
#     for j in range(i+1):
#         print(chr(char+n-j-1),end=" ")
#     print()

# n = 3
# char = ord("A")
# for i in range(n):
#     for j in range(i+1):
#         print(chr(char+j-i+n-1),end=" ")
#     print()


# n = 4
# for i in range(n):
#     for j in range(n):
#         if (i==0 or i==n-1) or (j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end= " ")
#     print()

# n = 4
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         top = i 
#         bottom = j
#         print("*",end=" ")
#     print()

# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         if j==0 or j==2*i or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n = 4
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         top = i
#         down = j
#         right = (2*n-2)-j
#         left = (2*n-2)-i
#         print(n-min(min(top,down),min(right,left)),end=" ")
#     print()

# 


# n = int(input("Enter the number:"))
# original = n
# reverse = 0
# while n > 0:
#     last = n%10
#     reverse = (reverse*10) + last
#     n = n//10
# if reverse == original:
#     print(True)
# else:
#     print(False)

# n = 35
# original = n
# num = 0
# length = len(str(n))
# while n > 0:
#     last = n % 10
#     num += last**length
#     n = n// 10
# if original == num:
#     print(True)
# else:
#     print(False)

# n = 36
# l = []
# for i in range(1,n+1):
#     if  n % i == 0:
#         l.append(i)
# print(l)

# import math
# n = 36
# l = []
# for i in range(1,int(math.sqrt(n))+1):
#     if n%i == 0:
#         l.append(i)
#         if n//i != i:
#             l.append(n//i)
# print(sorted(l))

# n = 29
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print(True)
# else:
#     print(False)

# if n < 2:
#     print(False)
# else:
#     is_prime = True
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             is_prime = False
#             break
#     print(is_prime)

# a = 9
# b = 12
# while a > 0 and b > 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# if a == 0:
#     print(b)
# else:
#     print(a)


# def name(n,i):
#     if n < i:
#         return
#     print(n,end=" ")
#     name(n-1,i)
# name(9,1)

# def sums(n,sum):
#     if n < 1:
#         print(sum)
#         return
#     sums(n-1,sum+n)
# sums(3,0)

# n = 5
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(n))

# arr = [1,2,3,4]
# def reverse(arr,l,r):
#     if l >= r:
#         return 
#     arr[l],arr[r] = arr[r],arr[l]
#     return reverse(arr,l+1,r-1)
# reverse(arr,0,len(arr)-1)
# print(arr)

# arr = [1,2,3,4]
# def single_pointer(arr,i):
#     n = len(arr)
#     if i >= n//2:
#         return 
#     arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
#     single_pointer(arr,i+1)
# single_pointer(arr,0)
# print(arr)

# s = "Sees"
# def palindrome(s):
#     s1 = ''.join(i for i in s if i.isalnum()).lower()
#     def help(i,n):
#         if i >= n//2:
#             return True
#         if s1[i] != s1[n-i-1]:
#             return False
#         return help(i+1,n)
#     n = len(s1)
#     return help(0,n)
# print(palindrome(s))

# n = 4
# def fibonacci(n):
#     if n <= 1:
#         return n
#     last = fibonacci(n-1)
#     sec_last = fibonacci(n-2)
#     return last + sec_last
# print(fibonacci(n))

# n = int(input("Enter the number: "))
# arr = []
# for i in range(n):
#     a = int(input())
#     arr.append(a)
# hash = [0]*(max(arr)+1)
# for num in arr:
#     hash[num] += 1
# a = int(input("Enter: "))
# print(hash[a])

# s = "abcdabehf"
# arr = []
# hash = [0]*26
# a = int(input("Enter the size of array: "))
# for i in range(len(s)):
#     hash[ord(s[i]) - ord('a')] += 1
# for _ in range(a):
#     c = input('Enter:')
#     arr.append(c)
# for c in arr:
#     print(hash[ord(c)-ord('a')])

# s = 'abc@--a[[ehf'
# arr = []
# hash = [0]*256
# a = int(input("Enter the size of array: "))
# for i in range(len(s)):
#     hash[ord(s[i])] += 1
# for j in range(a):
#     c = input("Enter: ")
#     arr.append(c)
# for c in arr:
#     print(hash[ord(c)])

# arr = [3,4,3,7,9,2,3]
# hash = {}
# for i in arr:
#     hash[i] = hash.get(i,0)+1
# a = int(input())
# lis = []
# for i in range(a):
#     c = int(input())
#     lis.append(c)
# for c in lis:
#     print(hash.get(c,0))


# arr = ['a','b','[',']','a','e','e','a']
# hash = {}
# for i in arr:
#     hash[i] = hash.get(i,0)+1
# print(hash)

# arr = [13,46,24,52,20,9]
# n = len(arr)
# for i in range(n-1):
#     min = i
#     for j in range(i+1,n):
#         if arr[j] < arr[min]:
#             min = j
#         arr[min], arr[i] = arr[i], arr[min]
#     print(arr)


# arr = [13,46,24,52,20,9]
# n = len(arr)
# for i in range(n):
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#     print(arr)


arr = [14,9,5,12,6,8,13]
