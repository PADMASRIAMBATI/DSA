name = input("Enter your full name: ")
result = len(name)
print(f"Length: {result}")

result1 = name.find("b") #first occurrence of index
print(f"First occurrence of A: {result1}")

result2 = name.rfind("a") #last occurrence of index
print(f"Last occurrence of A: {result2}")

result3 = name.capitalize()
print(f"Capitalize: {result3}")

result4 = name.lower()
print(f"Lower Case: {result4}")

result5 = name.upper()
print(f"Upper Case: {result5}")

result6 = name.isdigit()
print(f"Is Digit: {result6}")

result7 = name.isalpha()
print(f"Is Alphabet: {result7}")

phone_number = input("Enter the Phone Number: ")
result8 = phone_number.count("1")
print(f"Count particular Character: {result8}")

result9 = phone_number.replace("1","_")
print(f"Count particular Character: {result9}")

print(help(str))