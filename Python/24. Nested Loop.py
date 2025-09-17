# Nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:
for j in range(3):
    for i in range(1,10):
        print(i,end="")
    print()
