arr = [1, 2, 2, 1, 3]
map = {}

for i in arr:
    map[i] = map.get(i,0)+1

result = [[k,v] for k,v in map.items()]
print(result)



arr1 = [4,4,5,5,6]
map = {}

for i in arr1:
    map[i] = map.get(i,0)+1
max_freq = max(map.values())
result = [k for k,v in map.items() if v == max_freq]
print(min(result))