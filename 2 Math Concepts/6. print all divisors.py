n = 36
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
print(a)


# To reduce time complexity 

import math
b=[]
for i in range(1,int(math.sqrt(n))+1):
    if n % i ==0:
        b.append(i)
        if n //i != i:
            b.append(n//i)
print(sorted(b))