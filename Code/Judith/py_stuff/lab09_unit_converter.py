#filename: lab09_unit_converter.py


user_input = input('what is the distance, original unit, and conversion unit?\n')
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

def yards_to_meters(user_input_value):
    conversion_factor = 0.9144
    meters = conversion_factor * user_input_value
    return meters

def inches_to_meters(user_input_value):
    conversion_factor = 0.0254
    meters = conversion_factor * user_input_value
    return meters

def meters_to(converted_value):
    if sep_input[2] in ['m','meters']:
        return converted_value
    elif sep_input[2] in ['ft','feet']:
        converted_value = converted_value * 3.28084
        return converted_value
    elif sep_input[2] in ['in','inches']:
        converted_value = converted_value * 39.3701
        return converted_value
    elif sep_input[2] in ['mi','miles']:
        converted_value = converted_value * 0.000621371
        return converted_value
    elif sep_input[2] in ['km','kilometers']:
        converted_value = converted_value * 0.001
        return converted_value
    elif sep_input[2] in ['yd','yards']:
        converted_value = converted_value * 1.09361
        return converted_value

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

elif sep_input[1] == 'yd' or sep_input[1] == 'yards':
    converted_value = yards_to_meters(user_input_value)
    print(f'{user_input_value} {sep_input[1]} is {converted_value} m')

elif sep_input[1] == 'in' or sep_input[1] == 'inches':
    converted_value = inches_to_meters(user_input_value)
    print(f'{user_input_value} {sep_input[1]} is {converted_value} m')

elif sep_input[1] in ['m','meters']:
    converted_value = user_input_value
    print(f'{user_input_value} {sep_input[1]} is {converted_value} m')



else:
    print('enter a valid input')

if sep_input[2] in ['m','meters','km','kilometers','in','inches','ft','feet','yd','yards','mi','miles']:
    converted_value = meters_to(converted_value)
    print(f'{user_input_value} {sep_input[1]} is {converted_value} {sep_input[2]}')

else:
    print('enter a valid input')




