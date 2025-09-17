weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {weight} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {weight} {unit}")
else:
    print(f"{unit} is in valid unit")


# Temperature Convertion Program
unit = input("Is this temperature is Celsius or Fahrenheit (C/F):  ")
temp = float(input("Enter the temperature: "))
if unit == "C":
    temp = round((9 * temp)/5+32,1)
    print(f"The Temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32)* 5/9,1)
    print(f"The Temperature in Fahrenheit is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
