
count = 0
def sum():
    global count
    if count == 4:
        return
    print(count)
    count += 1
    sum()
sum()

print("------ Print Name N times Using Recursion ------")
def name(i,n):
    if i > n:
        return
    print("Tinku")
    name(i+1,n)
name(1,4)

print("------ Print Linearly from 1 to N ------")
def lineraly(i,n):
    if i > n:
        return
    print(i,end=" ")
    lineraly(i+1,n)
lineraly(1,4)
print()
    
print("------ Print in terms of N to 1 ------")
def reverse(n,i):
    if n < i:
        return
    print(n,end=" ")
    reverse(n-1,i)
reverse(4,1)
print()

print("------ Print Linearly from 1 to N (by using Backtracking) ------")
def linearly1(i,n):
    if i < 1:
        return
    linearly1(i-1,n)
    print(i,end=" ")
n=3
linearly1(n,n)
print()

print("------ Print Linearly from N to 1 (by using Backtracking) ------")
def reverse1(i,n):
    if i > n:
        return 
    reverse1(i+1,n)
    print(i,end=" ")
n=3
reverse1(1,n)
print()


