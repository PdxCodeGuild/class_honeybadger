#filename: unit_converter.py

user_input = input('what is the distance and unit?\n')
#print(user_input)
sep_input = user_input.split(sep=' ')
user_input_value = float(sep_input[0])

def feet_to_meters(user_input_value):
    conversion_factor = 0.3048
    meters = conversion_factor * user_input_value
    return meters

def miles_to_meters(user_input_value):
    conversion_factor = 1609.34
    meters = conversion_factor * user_input_value
    return meters

def kilometers_to_meters(user_input_value):
    conversion_factor = 1000
    meters = conversion_factor * user_input_value
    return meters

print(sep_input[1])

if sep_input[1] == 'ft' or sep_input[1] == 'feet':
    converted_value = feet_to_meters(user_input_value)
    print(f'{user_input_value} {sep_input[1]} is {converted_value} m')

elif sep_input[1] == 'mi' or sep_input[1] == 'miles':
    converted_value = miles_to_meters(user_input_value)
    print(f'{user_input_value} {sep_input[1]} is {converted_value} m')

elif sep_input[1] == 'km' or sep_input[1] == 'kilometers':
    converted_value = kilometers_to_meters(user_input_value)
    print(f'{user_input_value} {sep_input[1]} is {converted_value} m')

else:
    print("enter a valid input")





#print(feet_to_meters(user_input))
#print(miles_to_meters(user_input))
#print(kilometers_to_meters(user_input))
