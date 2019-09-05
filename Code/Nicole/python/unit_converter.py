#create variable

def feet_to_meters(feet):
    meters = feet * .3048
    return meters

user_input = float(input("\nWhat is the distance in feet?\n"))

# print(user_input)

converted_input = feet_to_meters(user_input)

print(f"Your conversion is {converted_input}")
