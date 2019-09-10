import sys

# define functions TO meters

def feet_to_meters(feet):
    conversion_factor = .3048
    meters = feet * conversion_factor
    return meters

def mile_to_meters(mile):
    conversion_factor = 1609.34
    meters = mile * conversion_factor
    return meters

def meter_to_meters(meter):
    conversion_factor = 1
    meters = meter * conversion_factor
    return meters

def km_to_meters(km):
    conversion_factor = 1000
    meters = km * conversion_factor
    return meters

# define functions FROM meters

def meters_to_feet(meter):
    conversion_factor = 3.048
    feet = meter * conversion_factor
    return feet

def meters_to_miles(meter):
    conversion_factor = 0.0006213712
    miles = meter * conversion_factor
    return miles

def meters_to_km(meter):
    conversion_factor = 0.001
    km = meter * conversion_factor
    return km

# list of possible input and output units


input_output_unit_list = ["ft", "feet", "miles", "mile", "m", "meter", "meters", "km", "kms", "kilometers"]

# create variables with input

user_distance = input("\nWhat is the distance you would like to convert? (Please enter a number.)\n")

# check to see if the input is a number
if user_distance.isdigit():
    user_distance = int(user_distance)
else:
    print("\nYou did not enter a number. Please start over and try again.\n")
    sys.exit()

# continue with input variables

user_input_units = input("\nWhat unit of measurement would you like to convert FROM? Please enter feet, miles, meters, or kilometers: \n")

while user_input_units in input_output_unit_list:
    break
else:
    print("\nYou did not enter a correct value. Please start over and try again.\n")
    sys.exit()

# convert input unit to meters

if user_input_units == "ft" or user_input_units == "feet":
    convert_to_meters = feet_to_meters(user_distance)
elif user_input_units == "mile" or user_input_units == "miles":
    convert_to_meters = mile_to_meters(user_distance)
elif user_input_units =="m" or user_input_units == "meter" or user_input_units == "meters":
    convert_to_meters = meter_to_meters(user_distance)
elif user_input_units == "km" or user_input_units == "kilometers" or user_input_units == "kilos" or user_input_units == "kms":
    convert_to_meters = km_to_meters(user_distance)
else:
    print("\nYou did not enter a correct value.\n")

convert_to_meters = float(convert_to_meters)

user_output_units = input("\nWhat unit of measurement would you like to convert TO? Please enter feet, miles, meters, or kilometers: \n")

while user_output_units in input_output_unit_list:
    break
else:
    print("\nYou did not enter a correct value. Please start over and try again.\n")
    sys.exit()

if user_output_units == "ft" or user_output_units == "feet":
    convert_to_output = meters_to_feet(convert_to_meters)
elif user_output_units == "mile" or user_output_units == "miles":
    convert_to_output = meters_to_miles(convert_to_meters)
elif user_output_units =="m" or user_output_units == "meter" or user_output_units == "meters":
    convert_to_output = meter_to_meters(convert_to_meters)
elif user_output_units == "km" or user_output_units == "kilometers" or user_output_units == "kilos" or user_output_units == "kms":
    convert_to_output = meters_to_km(convert_to_meters)
else:
    print("\nYou did not enter a correct value.\n")

print(f"\nHere's your conversion:\n\n{user_distance} {user_input_units} converts to {convert_to_output} {user_output_units}.\n")
