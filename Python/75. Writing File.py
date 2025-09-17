# Python writing files (.txt, .json, .csv)

txt_data = "I like my pet,Tinku."
# Relative file path
file_path = "output.txt"
with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path} was created")

# Absolute file path
file_path1 = "C:/Users/PADMASRI/OneDrive/Desktop/sample/output.txt"
with open(file_path1, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path1}' was created")

print("----------- MODE = 'x' ----------")
# Modes
# x = it shows error if that file is already exist
txt_data1 = "I love Pizza!"
try:
    with open(file_path, "x") as file:
        file.write(txt_data1)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file is already exits!")

print("----------- MODE = 'a' ----------")
# a = Append the new data to the file
try:
    with open(file_path, 'a') as file:
        file.write("\n" + txt_data1)
        print("New data is added to the file")
except FileExistsError:
    print("That file is already exits!")

