# n = [1,0,2,3,2,0,0,4,5,1]
# temp = []
# for i in range(len(n)):
#     if n[i]!=0:
#         temp.append(n[i])
# for j in range(len(temp),len(n)):
#     temp.append(0)
# for k in range(len(temp)):
#     n[k]=temp[k]
# print(n)


n = [0,0,0,0,66,5, 11,0,1,2,3,0,6,1]
j = 0
for i in range(len(n)):
    if n[i]!= 0:
        n[j],n[i]=n[i],n[j]
        j+=1
print(n)