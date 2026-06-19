# Method 1: Using loop with increment to find GCD
n1 = 9
n2 = 12
gcd = 1
for i in range(min(n1,n2),0,-1):
    if n1%i==0 and n2%i==0:
        gcd = i
        break
print(f"Using loop with increment: {gcd}")

# Method 2 : Using loop with decrement to find GCD
for i in range(min(n1,n2),0,-1):
    if n1%i==0 and n2%i==0:
        gcd = i
        break
print(f"Using loop with decrement: {gcd}")

# Method 3: Using Euclidean algorithm to find GCD
while(n1 > 0 and n2 >0):
    if n1 > n2:
        n1 = n1 % n2
    else:
        n2 = n2 % n1
if n1 ==0:
    print(f"Using Euclidean algorithm: {n2}")
else:
    print(f"Using Euclidean algorithm: {n1}")