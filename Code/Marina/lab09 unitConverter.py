user_input = input("what is the distance in feet, miles or kilometers? ")
print(user_input)
what_to_convert_to = input("what units do you wish to convert to? please enter meters, miles or kilometers: ")
print(what_to_convert_to)
separated_input = user_input.split(sep=' ')
user_input_value = float(separated_input[0])

def feet_to_meters(user_input_value):
    conversion_factor = 0.3048
    meters = conversion_factor * user_input_value
    feet = user_input_value / conversion_factor
    if what_to_convert_to == meters:
        return meters
    else:
        return feet

def miles_to_meters(mile):
    conversion_factor = 1609.34
    meters = conversion_factor * user_input_value
    miles = user_input_value / conversion_factor
    if what_to_convert_to == meters:
        return meters
    if what_to_convert_to == miles:
        return miles

def kilometers_to_meters(kilometers):
    conversion_factor = 1000
    meters = conversion_factor * user_input_value
    kilometers = user_input_value / conversion_factor
    if what_to_convert_to == meters:
        return meters
    if what_to_convert_to == kilometers:
        return kilometers

print(separated_input[1])
if separated_input[1] =='ft' or separated_input[1] == 'feet' and what_to_convert_to == 'meters':
    converted_value = feet_to_meters(user_input_value)
    print(f"{user_input_value} {separated_input[1]} is {converted_value} m")
if separated_input[1] == 'mile' or separated_input[1] == 'miles' and what_to_convert_to == 'meters' or what_to_convert_to == 'meter':
    converted_value = miles_to_meters(user_input_value)
    print(f"{user_input_value} {separated_input[1]} is {converted_value} {what_to_convert_to}")
if separated_input[1] == 'kilometers' or separated_input[1] == 'kilometer' or separated_input[1] == 'km' and what_to_convert_to == 'meters':
    converted_value = kilometers_to_meters(user_input_value)
    print(f"{user_input_value} {separated_input[1]} is {converted_value} {what_to_convert_to}")
else:
    print("Please enter feet, miles or kilometers")


# converted_input = feet_to_meters(user_input)
#
# print(f"your calculation is {converted_input})
