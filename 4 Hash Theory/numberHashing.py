n = int(input("Size of the array:"))
arr = []
for i in range(n):
    a = int(input(f"Enter {i} element:"))
    arr.append(a)

hash = [0]*(max(arr)+1)
for num in arr:
    hash[num] += 1

q = [5, 1 , 4, 2, 3, 12]
for j in q:
    if j < len(hash):
        print(f"{j} appers {hash[j]} times")
    else:
        print(f"{j} appers {0} times")



                                                                                                                                                                                                         

