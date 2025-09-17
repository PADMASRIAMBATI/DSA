# function = A block of reusable code
#            place () after the function name to invoke it

# Example-1
def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print(" ")
happy_birthday("Tinku",8)
happy_birthday("Padmasri",21)
happy_birthday("Devi",38)

print("------------------------------------")
# Example-2
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
   
display_invoice("Padmasri", 34.3, "01/01/2025")
