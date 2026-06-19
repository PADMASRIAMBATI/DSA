num = [3,1,2]
n = len(num)
ds = []
index = 0
def fun(index,ds,num,n):
    if index == n:
        if len(ds) == 0:
            print('{}')
        else: 
            print(ds)
        return
    
    ds.append(num[index])
    fun(index+1,ds,num,n)
    ds.pop()
    fun(index+1,ds,num,n)
fun(index,ds,num,n)