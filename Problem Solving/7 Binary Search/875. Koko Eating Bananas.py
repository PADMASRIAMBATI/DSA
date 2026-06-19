print("-----Brute Force------")
piles = [3,6,7,11]
h = 8
m = max(piles)
def fun(piles,hourly):
    total_hr = 0
    for i in range(len(piles)):
        total_hr += (piles[i]+hourly-1)//hourly
    return total_hr
for i in range(1,m+1):
    total = fun(piles,i)
    if total <= h:
        print(i)
        break

print("-----Optimal Approach------")
piles = [3,6,7,11]
h = 8
high = max(piles)
low = 1
def fun(piles,hourly):
    total_hr =0
    for i in range(len(piles)):
        total_hr += (piles[i]+hourly-1)//hourly
    return total_hr
while low < high:
    mid = (low+high) // 2
    total = fun(piles,mid)
    if total > h:
        low = mid + 1
    else:
        high = mid
print(low)
    

