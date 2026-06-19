n = 1500
if n <= 1:
    print(n)
else:
    for i in range(2,int(n**0.5)+1):
        while n %i == 0:
            n = n//i
            print(i,end=" ")





# n = list(map(int,input().split()))
# size = n[0]
# target = n[1]
# chemical = n[2:size+2]
# toxic = n[size+2:]
# if size > 0:
#     hash = []
#     prefix_sum = 0
#     min_c = float('inf')
#     for i in range(size):
#         if i != i-1 or i != i+1:
#             prefix_sum += chemical[i]
#             if hash[target - prefix_sum] in hash:
#                 min_c = min(min_c,i-hash(target-prefix_sum))
        
#             hash[prefix_sum] = i
#             if i != i-1 or i != i+1:
#                 print(min_c,end=" ")
#                 print(i, j)
            
            
            
# else:
#     print("Invalid input.")