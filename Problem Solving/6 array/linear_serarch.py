n = [1,2,5,7,2,3,4,9,8]
k = 4
for i in range(len(n)):
    if n[i] == k:
        print(i)
if k not in n:
    print("Not Exist")
    