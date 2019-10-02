
# type_of_conversion = input("What type of conersion would you like to make? (A)feet-meters, (B)miles-meters, (C)kilometers-meters: ")




user_input = int(input("What is the distance in feet? "))

def feet_to_meters(feet):
    feet = user_input
    conversion = 0.3048 * user_input
    return conversion


# def miles_to_meters(mile):
#      conversion = 1609.34
#      meters = converted_factor * miles
#      return meters
#
# def kilometers_to_meters(kilometers):
#      conversion = 1000
#      meters = conversion * user_input_value
#      return meters
#if seperated_input[1] == "ft" or seperated_input[1] == "feet":



converted_value = feet_to_meters(user_input)

print(converted_value)
