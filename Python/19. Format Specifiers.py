#format specifiers = {value:flags} from a value based on what flags are inserted

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

#
print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.3f}")

print("**********Empty Space's***********")
# spaces before to print
print(f"Price 1 with spaces is ${price1:10}")
print(f"Price 2 with spaces is ${price2:10}")
print(f"Price 3 with spaces is ${price3:10}")

print("*********Empty Space 0's************")

print(f"Price 1 with 0 spaces is ${price1:010}")
print(f"Price 2 with 0 spaces is ${price2:010}")
print(f"Price 3 with 0 spaces is ${price3:010}")

print("*********Left Justyfied************")

print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

print("*********Right Justyfied************")

print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

print("*********Center************")

print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

print("*********Plus Sign************")

print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

print("*********Separated by comma************")

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

print("*********Combination of Flags************")

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

