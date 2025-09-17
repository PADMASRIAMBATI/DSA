# OR operator
temp = 20
is_raining = False
if temp > 30 or temp < 0 or is_raining:
    print("The Outdoor event is Cancelled")
else:
    print("The Outdoor Event is still scheduled")

# AND operator
temp1 = 20
is_sunny = False
if temp1 >=28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp1 <= 0 and is_sunny:
    print("It's cool outside")
    print("It is SUNNY")
elif temp1 < 28 and temp > 0 and is_sunny:
    print("It's WARM outside")
    print("It is SUNNY")

# NOT operator
elif temp1 >=28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif temp1 <= 0 and not is_sunny:
    print("It's cool outside")
    print("It is CLOUDY")
elif temp1 < 28 and temp > 0 and not is_sunny:
    print("It's WARM outside")
    print("It is CLOUDY")


