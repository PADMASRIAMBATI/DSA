# Python file detection
import os

# Relative file path
file_path1 = "stuff74/test74.txt"

# Absolute file path
file_path2 = "C:\\Users\\PADMASRI\\OneDrive\\Desktop\\sample\\test.txt"
#            or C:/Users/PADMASRI/OneDrive/Desktop/sample/test.txt

if os.path.exists(file_path1): # change to file_path1
    print(f"This Location '{file_path1}' exists")
    if os.path.isfile(file_path1):
        print("This is a file")
    elif os.path.isdir(file_path1):
        print("That is a directory")
else:
    print("This Location doesn't exists")