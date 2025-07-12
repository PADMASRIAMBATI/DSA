# 2-Dimensional Key Pad for Phone
# tuple is fast and unchanged so we use tuple
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for i in num_pad:
    for j in i:
        print(j,end=" ")
    print()