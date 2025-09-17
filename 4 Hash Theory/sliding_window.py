arr = [1, 1, 1, 2, 2, 4]
k = 2

l, r , total, res = 0, 0, 0, 0
while r < len(arr):
    total += arr[r]  
    #print(f"total {total}")
    #print(f"{arr[r] * (r-l+1)} > {total - k}")
    while arr[r] * (r-l+1) > total + k:
        #print(f"{arr[r]} * {r}-{l}+1 > {total} - {k}")
        total -= arr[l]
        print(f"{total}")
        l += 1
    res = max(res,r-l+1)
    r+=1
print(res)