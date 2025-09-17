from car60 import Car
# Objects = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class =(Blueprint) used to design the structure and layout of an object

# Objects
car1 = Car("BMW", 2024, "blue", True)
car2 = Car("Benz", 2025, "black", True)
car3 = Car("Charger",2026, "yellow", True)

print(f"Storage ID: {car1}")

print("--- Objects ---")
print(f"{car1.model},{car1.year},{car1.color},{car1.for_sale}")
print(car2.model)
print(car3.color)

print("--- Methods ---")
# Methods
car1.drive()
car1.stop()
car2.describe()