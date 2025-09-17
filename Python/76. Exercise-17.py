
# List
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
file_path = "output.txt"
with open(file_path, "w") as file:
    for employee in employees:
        file.write(employee + " ")
    print(f"txt file '{file_path}' was created")

# json
import json
file_path = "output.json"
employee1 = {
    "name" : "Spongebob",
    "age" : 30,
    "job" : "cook"
}
with open(file_path, "w") as file:
    json.dump(employee1, file, indent=4)
    print(f"json file '{file_path}' was created")

# csv
import csv
employee2 = [["Name", "Age", "Job"],
             ["Spongebob", 30, "cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path2 = "output.csv"
with open(file_path2, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employee2:
        writer.writerow(row)
    print(f"csv file '{file_path}' was created")