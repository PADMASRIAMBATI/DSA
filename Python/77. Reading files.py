# Python reading files (.txt, .json, .csv)
print("********** TXT **********")
file_path = "C:\\Users\\PADMASRI\\OneDrive\\Desktop\\sample\\output.txt"
file_path1 = "output.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

print("********** JSON **********")
# Json
import json
file_path2 = "output.json"
try:
    with open(file_path2, "r") as file:
        content1 = json.load(file)
        print(content1)
        print(content1["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

print("********** CSV **********")
# csv
import csv
file_path3 = "output.csv"
try:
    with open(file_path3, "r") as file:
        content2 = csv.reader(file)
        for line in content2:
            print(line)
except FileNotFoundError:
    print("That file is not found")
except PermissionError:
    print("You do not have permission to read that file")