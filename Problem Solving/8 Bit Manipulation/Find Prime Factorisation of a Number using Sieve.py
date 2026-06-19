num =  [7, 12, 18]
max_num = max(num)
list = list(range(max_num+1))
for i in range(2,int(max_num**0.5)+1):
    if list[i] == i:
        for j in range(i*i,max_num+1,i):
            if list[j] == j:
                list[j] = i
result = []
for n in num:
    temp = []
    while n > 1:
        temp.append(list[n])
        n = n//list[n]
    result.append(temp)
print(result)
