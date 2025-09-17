# Validate user input exercise
#1. username is not more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

Username = input("Enter a username: ")
if len(Username)>=12:
    print("Username can't contain be more than 12 characters")
elif not Username.find(" ")==-1:
    print("Username can't contain spaces")
elif not Username.isalpha():
    print("Username can't contain Digits")
else:
    print(f"Welcome {Username}")