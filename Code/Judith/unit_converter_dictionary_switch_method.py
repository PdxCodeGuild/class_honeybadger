#filename: unit_converter_dictionary_switch_method.py

user_input = input('what is the distance and unit?\n')
#print(user_input)
sep_input = user_input.split(sep=' ')
user_input_value = float(sep_input[0])

def jump():
    switcher = {
        'feet' : 0.3048,
        'miles' : 1609.34,
        'kilometers' : 1000
        }
