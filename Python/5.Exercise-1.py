# Calc Rectangle Area
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area = length * width
print(f"Area of the Rectangle {area}cm")

print("****************************************")

#Shopping Cart Program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} X {item}/s" )
print(f"Your total is: ${total}")