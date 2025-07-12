# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

# Example-1
def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")
hello("Hello", "Ms.", "Padmasri", "Ambati")
hello(title="Ms.", last="Ambati",first= "Padmasri",greeting="Hello",)  # KEYWORD ARGUMENTS

# Example-2
def num():
    for i in range(1,11):
        print(i, end=" ")
    print()
num()

print("1","2","3","4","5", sep="-")

print("-------------------------------------")
# Generate Phone Number
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(area=8, last=8765, country="+91", first=93562)
print(phone_num)

print("-------------------------------------")