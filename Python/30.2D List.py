fruits =     ["apple","orange","banana","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats =      ["chicken","fish","turkey"]

groceries1 = [fruits,vegetables,meats]
#print(groceries[0][3])
for i in groceries1:
    for j in i:
        print(j,end=" ")
    print()

print('-------- LIST --------')
# List
groceries2 = [["apple","orange","banana","coconut"],
              ["celery","carrots","potatoes"],
              ["chicken","fish","turkey"]]
for i in groceries2:
    for j in i:
        print(j,end=" ")
    print()


print('-------- TUPLE --------')
# Tuple
groceries3 = (("apple","orange","banana","coconut"),
              ("celery","carrots","potatoes"),
              ("chicken","fish","turkey"))
for i in groceries3:
    for j in i:
        print(j,end=" ")
    print()

print('-------- SET --------')
# Set
groceries4 = ({"apple","orange","banana","coconut"},
              {"celery","carrots","potatoes"},
              {"chicken","fish","turkey"})
for i in groceries4:
    for j in i:
        print(j,end=" ")
    print()
