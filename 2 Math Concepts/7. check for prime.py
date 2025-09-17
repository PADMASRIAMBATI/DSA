# Here Time Complexity is O(n)
x=10
i=1
count=0
while i<=x:
    if x%i==0:
        count+=1
    i+=1
if count==2:
    print(True)
else:
    print(False)


# Here Time Complexity is O(sqrt(n))
# This code checks if a number is prime by counting its divisors
n= 73
i=1
count=0
while i*i<= n:
    if n%i==0:
        count+=1
        if n//i != i:
            count+=1
    i+=1

if count==2:
    print(True)
else:
    print(False)