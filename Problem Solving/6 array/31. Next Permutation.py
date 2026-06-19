def nextpermutation(num):
    n = len(num)
    index = -1
    def reverse(num,l,r):
        if l >= r:
            return 
        num[l],num[r]=num[r],num[l]
        reverse(num,l+1,r-1)
    for i in range(n-2,-1,-1):
        if num[i] < num[i+1]:
            index = i
            break
    if index == -1:
        reverse(num,0,n-1)
        return
    for i in range(n-1,index,-1):
        if num[i] > num[index]:
            num[index], num[i] = num[i], num[index]
            break
    reverse(num,index+1,n-1)

num = [2,1,5,4,3,0,0]
num1 = [3,2,1]
nextpermutation(num)
print(num)