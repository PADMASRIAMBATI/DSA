print('-----Print Primes-----')
n = 30
if n<=2:
    print('No primes')
else:
    p=[1]*(n+1)
    p[0] = p[1] = 0
    for i in range(2,int(n**0.5)+1):
        if p[i]==1:
            for j in range(i*i,n+1,i):
                p[j]=0
    for i in range(2,n+1):
        if p[i] == 1:
            print(i,end=" ")

print()
print('-----Count Primes-----')
n = 30
p=[1]*(n)
p[0] = p[1] = 0
for i in range(2,int(n**0.5)+1):
    if p[i]==1:
        for j in range(i*i,n,i):
            p[j]=0
print(sum(p))