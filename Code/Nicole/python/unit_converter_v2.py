import sys

# define functions

def feet_to_meters(feet):
    converstion_factor = .3048
    meters = feet * converstion_factor
    return meters

def mile_to_meters(mile):
    converstion_factor = 1609.34
    meters = mile * converstion_factor
    return meters

def meter_to_meters(meter):
    converstion_factor = 1
    meters = meter * converstion_factor
    return meters

def km_to_meters(km):
    converstion_factor = 1000
    meters = km * converstion_factor
    return meters

# #create variable with input
user_input = input("\nWhat is the distance you would like to convert?\n")
separated_input = user_input.split(sep = " ")

# convert number to float
if separated_input[0].isdigit():
    separated_input[0] = float(separated_input[0])
else:
    print("\nPlease enter a correct value.\n")
    sys.exit()


if separated_input[1] == "ft" or separated_input[1] == "feet":
    converted_value = feet_to_meters(separated_input[0])
    print(f"\n{user_input} is {converted_value} meters")
elif separated_input[1] == "mile" or separated_input[1] == "miles":
    converted_value = mile_to_meters(separated_input[0])
    print(f"\n{user_input} is {converted_value} meters")
elif separated_input[1] == "m" or separated_input[1] == "meter" or separated_input[1] == "meters":
    converted_value = meter_to_meters(separated_input[0])
    print(f"\n{user_input} is {converted_value} meters")
elif separated_input[1] == "km" or separated_input[1] == "kilometers" or separated_input[1] == "kilometer":
    converted_value = km_to_meters(separated_input[0])
    print(f"\n{user_input} is {converted_value} meters")
else:
    print("You did not enter a correct value.")
