'''Given an array nums of size n, which denotes the positions of stalls, and an integer k, which denotes the number of aggressive cows, assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. Find the maximum possible minimum distance.


Example 1

Input: n = 6, k = 4, nums = [0, 3, 4, 7, 10, 9]

Output: 3

Explanation:

The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions [0, 3, 7, 10]. Here the distances between cows are 3, 4, and 3 respectively.

In no manner can we increase the minimum distance beyond 3.

Example 2

Input : n = 5, k = 2, nums = [4, 2, 1, 3, 6]

Output: 5

Explanation: The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions [1, 6]. '''

print("-----Brute Force------")
num = [0,3,4,7,10,9]
cows = 4
num.sort()
max_dis = num[-1]-num[0]
def place(num,distance,cows):
    lastcow = num[0]
    count_cow = 1
    for i in range(len(num)):
        if num[i]-lastcow >= distance:
            count_cow += 1
            lastcow = num[i]
        if count_cow >= cows:
            return True
    return False
for i in range(1,max_dis+1):
    if not place(num,i,cows):
        print(i-1)
        break
else:
    print(max_dis)


print("-----Optimal Approach------")
num = [0,3,4,7,10,9]
cows = 4
num.sort()
def place(num,distance,cows):
    last_cow = num[0]
    count_cow = 1
    for i in range(1,len(num)):
        if num[i]-last_cow >= distance:
            count_cow += 1
            last_cow = num[i]
        if count_cow >= cows:
            return True
    return False
low = 1
high = num[-1]-num[0]
ans = 0
while low <= high:
    mid = (low+high)//2
    if place(num,mid,cows):
        ans = mid
        low = mid+1
    else:
        high = mid-1
print(ans)