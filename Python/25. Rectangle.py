rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbols = input("Enter the symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(f"{symbols}",end=" ")
    print()