# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class
class Student:
    class_year = 2025
    num_student = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Padmasri", 20)
student2 = Student("Tinku", 8)
student3 = Student("Devi", 30)
student4 = Student("Babji", 40)

print(student1.name) # (instance variable)
print(student1.age) # (instance variable)

print(student1.class_year) # by using object (class variable)
print(Student.class_year)  # by using class (class variable)

print(f"Number of students: {Student.num_student}")

print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

