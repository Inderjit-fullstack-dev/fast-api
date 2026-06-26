# Create a list of 5 animals called zoo
# - Delete the animal at the 3rd index.
# - Append a new animal at the end of the list
# - Delete the animal at the beginning of the list.
# - Print all the animals
# - Print only the first 3 animals

# the following statement will import all the function inside calc.py
# from calc import *
from calc import square

print(square(5))

zoo = ["Lion", "Monkey", "Elephant", "Tiger", "Deer"]
zoo.pop(2)
zoo.append("Penguin")
zoo.pop(0)

print(zoo)
print(zoo[0:3])

# Dictionaries in python


# Based on the dictionary:
# my_vehicle = {
#     "model": "Ford",
#     "make": "Explorer",
#     "year": 2018,
#     "mileage": 40000
# }
# - Create a for loop to print all keys and values
# - Create a new variable vehicle2, which is a copy of my_vehicle
# - Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
# - Delete the mileage key and value from vehicle2
# - Print just the keys from vehicle2

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}


for k,v in my_vehicle.items():
    print(f"{k}: {v}")

vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
vehicle2.pop("mileage")

for k in vehicle2:
    print(k)
