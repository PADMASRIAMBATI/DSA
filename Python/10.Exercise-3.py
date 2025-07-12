# Circumference of a circle

import math
radius = float(input("Enter radius: "))
pi = math.pi
result = 2 * pi * radius
print(f"Circumference of a circle: {result}")
print(f"Circumference of a circle: {round(result)}cm")


# Area of circle
result1 = pi * pow(radius,2)
print(f"Area of circle: {round(result1,2)}cm^2")

# to find hypothisis of right angle triangle
A = float(input("Enter side A: "))
B = float(input("Enter side B: "))
result2 = math.sqrt(pow(A,2) + pow(B,2))
print(f"Side C: {result2}")
