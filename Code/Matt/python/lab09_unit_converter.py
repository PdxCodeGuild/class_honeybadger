
def unit_converter(user_input,user_unit):
    conversion_dict = {
        'ft': 0.3048,
        'miles': 1609.34,
        'meter': 1,
        'kilometer': 1000
    }
    if user_unit in ['feet', 'ft', 'feets']:
        user_unit = 'ft'
    if user_unit not in conversion_dict:
        return None



    v = conversion_dict[user_unit]
    converted_distance = user_input * v
    return converted_distance


user_unit = input('What is the unit you want to convert to: ')
user_input = input('What is the number of meters you want converted?: ')




print(unit_converter(user_input,user_unit))
