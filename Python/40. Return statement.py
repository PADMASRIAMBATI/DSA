# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiple(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(f"Addition: {add(2,5)}")
print(f"Subtraction: {subtract(2,5)}")
print(f"Multiplication: {multiple(2,5)}")
print(f"Division: {divide(2,5)}")

print("----------------------------------------------")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("padmasri", "ambati")
print(full_name)

print("----------------------------------------------")