N = 7789
count=0
while N > 0:
    N = N // 10
    count += 1
print(count)

# time complexcity is O(log N) as we are dividing N by 10 in each iteration.
import math
n = 7789
count1 = int(math.log10(n)+1)
print(count1)


print("Time complexity is O(log N) as we are dividing N by 10 in each iteration is ",math.log10(n))
#if it is divisible by 2 then the time complexity is log2(n)..............