line = "[1, 2, 3, 4, 5 , 'a', 'b', 'c', 6, 7, 8]"
numstr = ""
arr = []
for i in line:
    if i.isdigit():
        numstr += i
    elif numstr:
        arr.append(numstr)
        numstr = ""
if numstr:
    arr.append(numstr)

print("array elements are:",*arr)



line = [1, 2, 3, 4, 5 , 'a', 'b', 'c', 6, 7, 8]
arr = []
for i in line:
    if isinstance(i,int):
        arr.append(i)
print("array elements are:",*arr)