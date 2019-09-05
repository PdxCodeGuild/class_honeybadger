# user_input = input("What is the distance in feet ")
# print(user_input)
# print(user_input.split(sep= ' '))#splitting user input by space delimiter and creates a list
# separated_input = user_input.split(sep= ' ') #assigning the split variables to a value. Will need this for indexing
# user_input_value = float(separated_input[0])# converting the first value in array from character to float. Will need to do this because of mulitplication
# print(user_input_value)

# #define function to conver user input to meters
# def feet_to_meters(user_input_value): #module is accepting a parameter called user_input_value
#     conversion_factor = 0.3048
#     meters = conversion_factor * user_input_value
#     return meters #when function is called, will return value 

# def miles_to_meters(user_input_value):
#     conversion_factor = 1609.34
#     meters = conversion_factor * user_input_value
#     return meters

# def kilometers_to_meters(user_input_value):
#     conversion_factor = 1000
#     meters = conversion_factor* user_input_value
#     return meters

# #testing to make sure functions do what I expect 
# # print(feet_to_meters(1)) #should return .3048
# # print(miles_to_meters(1)) #should return 1609.34
# # print(kilometers_to_meters(1)) #should return 1000

# # print(separated_input[1]) # [] provides the location of the variable in the array
# if separated_input[1] == 'ft' or separated_input =='feet': #[1] is the second location of array
#    converted_value = feet_to_meters(user_input_value) #calling feet_to_meters module and sending the 1st value of the array to module, which has been converted to a float
#    print(f"{user_input_value} {separated_input[1]} is {converted_value}") #informing user if they provided fit, meter, etc

# if separated_input[1] == 'miles' or separated_input == 'miles':
#     converted_value = miles_to_meters(user_input_value)
#     print(f"{user_input_value} {separated_input[1]} is {converted_value}")

# if separated_input[1] == 'kilometers' or separated_input[1] == 'kilos':
#     converted_value = kilometers_to_meters(user_input_value)
#     print(f"{user_input_value} {separated_input[1]} is {converted_value}")

#Part 4
user_input = input("What is the distance? ")
# print(user_input)
print(user_input.split(sep= ' '))#splitting user input by space delimiter and creates a list
separated_input = user_input.split(sep= ' ') #assigning the split variables to a value. Will need this for indexing
user_input_value = float(separated_input[0])# converting the first value in array from character to float. Will need to do this because of mulitplication
print(user_input_value)

#define function to conver user input to meters
def feet_to_meters(user_input_value): #module is accepting a parameter called user_input_value
    conversion_factor = 0.3048
    meters = conversion_factor * user_input_value
    return meters #when function is called, will return value 

def miles_to_meters(user_input_value):
    conversion_factor = 1609.34
    meters = conversion_factor * user_input_value
    return meters

def kilometers_to_meters(user_input_value):
    conversion_factor = 1000
    meters = conversion_factor* user_input_value
    return meters

#testing to make sure functions do what I expect 
# print(feet_to_meters(1)) #should return .3048
# print(miles_to_meters(1)) #should return 1609.34
# print(kilometers_to_meters(1)) #should return 1000

# print(separated_input[1]) # [] provides the location of the variable in the array
if separated_input[1] == 'ft' or separated_input =='feet': #[1] is the second location of array
   converted_value = feet_to_meters(user_input_value) #calling feet_to_meters module and sending the 1st value of the array to module, which has been converted to a float
   print(f"{user_input_value} {separated_input[1]} is {converted_value}") #informing user if they provided fit, meter, etc

if separated_input[1] == 'miles' or separated_input == 'miles':
    converted_value = miles_to_meters(user_input_value)
    print(f"{user_input_value} {separated_input[1]} is {converted_value}")

if separated_input[1] == 'kilometers' or separated_input[1] == 'kilos':
    converted_value = kilometers_to_meters(user_input_value)
    print(f"{user_input_value} {separated_input[1]} is {converted_value}")

if separated_input[1] == 'feet' or separated_input[1] =='ft':
    converted_value_feet = user_input_value/.3048
    print(f"{converted_value_feet} ft is {}"converted_value_feet)

if separated_input[1] == 'miles':
    converted_value_miles = user_input_value/1608.34
    print(converted_value_feet)

if separated_input[1] == 'kilos':
    converted_value_kilos = user_input_value/1000
    print(converted_value_kilos)

# print(f"You entered {separated_input[0]},{separated_input}[1]")

# #Checking to see what results should be
# print(feet_to_meters(1)) #calling feet_to_meters module and passing the value of 1
# answer = feet_to_meters(user_input)

# #convert user input to meters/apply function
# converted_input = feet_to_meters(user_input)

# #display converted value to user
# print(f"you calculation is{converted_input}")

########SOLUTION###################

"""
Lab 9: convert the given distance and units to the target units
we have four types of units: meters (m), miles (mi), feet (ft), and kilometers (km)
we could handle each case individually
    e.g. if from_units == 'm' and to_units == 'miles'
instead, we'll just convert to meters, then convert to the target units
"""

# 1) get the distance from the user
# 2) convert that distance to a float
# 3) get the units for that distance from the user
# 4) get the units that the user wants to convert to
# 4) convert the distance to meters
# 5) convert the distance from meters to the target


# 1 mile is 1609.34 meters
# 1 foot is 0.3048 meters
# 1 kilometer is 1000 meters
# 1 meter is 1 meter
# 1 yard is 0.9144 meters
# 1 inch is 0.0254 meters


# convert the given distance from the given units to meters
def to_meters(distance, units):
    if units == 'm':  # meters
        return distance
    elif units == 'mi': # miles
        return distance * 1609.34
    elif units == 'ft': # feet
        return distance * 0.3048
    elif units == 'km': # kilometers
        return distance * 1000
    elif units == 'yd': # yards
        return distance * 0.9144
    elif units == 'in': # inches
        return distance * 0.0254


# convert the given distance (in meters) to the target units
def from_meters(distance, units):
    if units == 'm': # meters
        return distance
    elif units == 'mi': # miles
        return distance / 1609.34
    elif units == 'ft': # feet
        return distance / 0.3048
    elif units == 'km': # kilometers
        return distance / 1000
    elif units == 'yd': # yards
        return distance / 0.9144
    elif units == 'in': # inches
        return distance / 0.0254


def standardize_units(units):
    if units in ['m', 'meter', 'meters']:
        return 'm'
    elif units in ['mi', 'mile', 'miles']:
        return 'mi'
    elif units in ['ft', 'feet']:
        return 'ft'
    elif units in ['km', 'kilometer', 'kilometers']:
        return 'km'
    elif units in ['yd', 'yard', 'yards']:
        return 'yd'
    elif units in ['in', 'inch', 'inches']:
        return 'in'

def main():
    print('Welcome to the Distance Converter 5001™')
    distance_in = float(input('what is the distance? '))
    units_in = input('what are the units you\'re converting from? ')
    units_out = input('what are the units you\'re converting to? ')

    units_in = standardize_units(units_in)
    units_out = standardize_units(units_out)


    distance_in_m = to_meters(distance_in, units_in)
    distance_out = from_meters(distance_in_m, units_out)

    output = f'{distance_in} {units_in} is {distance_out} {units_out}'

    # output = str(distance_in) + ' ' + units_in + ' is '
    # output += str(distance_out) + ' ' + units_out
    print(output)


main()
