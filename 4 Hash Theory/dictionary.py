arr = [3, 4, 3, 7, 9, 2, 3]

dic = {}

for i in arr:
    dic[i] = dic.get(i,0)+1   
    # hash_map.get(value,default)
print(dic)


arr1 = ['a', 'b', '[', ']', 'a', 'e' ,'e' ,'a']
hash_map = {}
for j in arr1:
    hash_map[j] = hash_map.get(j,0)+1
print(hash_map)

from collections import Counter
map = Counter(arr1)
print(map)

from collections import defaultdict
map1 = defaultdict(list)
for i in arr1:
    map1[i].append(1)
print(map1)


from collections import defaultdict
map2 = defaultdict(int)
for i in arr1:
    map2[i] += 1
print(map2)





arr2 = [3, 4, 3, 7, 9, 2, 3]

hash_map = {}
for j in arr2:
    hash_map[j] = hash_map.get(j,0)+1

n1 = int(input("size:"))
q = []
for num in range(n1):
    num = int(input(f"enter {num} element:"))
    q.append(num)

for i in q:
    print(hash_map.get(i,0))