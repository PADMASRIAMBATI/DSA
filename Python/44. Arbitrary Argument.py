# *args   = allows you to pass multiple non-key arguments
# **kwargs= allows you to pass multiple keywords-arguments
#           *unpacking operator
#           1. positional, 2. default, 3. keyword, 4. ARBITRARY
print("----------------------------------------------")
def add(*args):
    return type(args)
print(add(1,2,3,4,5,6))

print("----------------------------------------------")

def add1(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(f"Total: {add1(1, 2, 3)}")

print("----------------- *args ----------------------")
def display_name(*names):
    for name in names:
        print(name, end=" ")
    print()
display_name("MS.","Padmasri","Ambati","(Sweety)")

print("-------------- *Keyword args ------------------")

def print_address(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key:7}: {value}")
print_address(street="Ramalayam veedhi",
              apt="22-2-9",
              city="Peddapuram",
              state="Andhra Pradesh",
              zip="533437")