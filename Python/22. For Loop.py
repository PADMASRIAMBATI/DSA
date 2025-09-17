#for loop = execute a block of code a fixed number of times.
#    you can iterate over a range,string,sequence,etc

for i in range(1,11):
    print(i,end=" ")
print("Happy New Year")

for i in range(1,11,2):
    print(i,end=" ")
print("Happy New Year")

for i in reversed(range(1,11)):
    print(i,end=" ")
print("Happy New Year")


credit_card = "1234-5678-9012-3456"
for j in credit_card:
    print(j,end="")
print(" ")


for k in range(1,21):
    if k == 13:
        break
    else:
        print(k,end=" ")
