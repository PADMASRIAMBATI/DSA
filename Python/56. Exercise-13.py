# Python Banking Program

def show_balance(balance):
    print("*******************************")
    print(f"Your Balance is ${balance:.2f}")
    print("*******************************")

def deposit():
    print("*******************************")
    amount = float(input("How much to deposit: "))
    print("*******************************")

    if amount <= 0:
        print("*******************************")
        print(f"That's not a valid amount")
        print("*******************************")
        return 0
    else:
        return amount



def withdraw(balance):
    print("*******************************")
    amount = float(input("How much you want to withdraw: "))
    print("*******************************")

    if amount > balance:
        print("*******************************")
        print("Insufficient funds")
        print("*******************************")
        return 0
    elif amount <= 0:
        print("*******************************")
        print("Amount must be greater than 0")
        print("*******************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("***************************")
        print("      BANKING PROGRAM      ")
        print("***************************")
        print("1.Show Balance", end=" ")
        print("2.Deposit", end=" ")
        print("3.Withdraw",end=" ")
        print("4.Exit")
        print("***************************")

        choice = input("Enter Your Choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("***************************")
            print("This is not a Invalid choice")
            print("***************************")
    print("***************************")
    print("Thank you! Have a nice day!")
    print("***************************")


if __name__ == "__main__":
    main()