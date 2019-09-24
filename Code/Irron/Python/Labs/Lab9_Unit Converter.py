'''
Lab 9: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.
Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters. 
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. 

Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m

Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m

Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m

Version 3

Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m

'''

def unit_converter(distance, units):
    if units == 'meters':
        meters = 0.3048  #1 ft = .3048 meters
        feet_meters = distance*meters
        print(f'{distance} ft equals {feet_meters} m.')
    elif units == 'miles':
        miles = 1609.34 #1 mile = 1609.34 meters
        miles_meters = distance*miles
        print(f'{distance} mile equals {miles_meters} m.')
    elif units == 'kilometers':
        kilometes = 1000 #1 km = 1000 meters
        kilos_meters = distance*kilometes
        print(f'{distance} kilometers equals {kilos_meters} m.')
    elif units == 'yards':
        yards = 0.9144 #1 yard = .9144 meters
        yards_meters = distance*yards
        print(f'{distance} yards equals {yards_meters} m.')
    elif units == 'inches':
        inches = 0.0254 #1 inch = .0254 meters
        inches_meters = distance*inches
        print(f'{distance} inches equals {inches_meters} m.')

    return 


input_values = input('Please enter the distance and units (feet, miles, meters, yards, inches or kilometers),seperated by a comma ') #Do Not enter a space between comma

#parsing user input and converting distance into integer. Otherwise the unit_converter function will crash because of math computations.
input_split = input_values.split(',') # spliting user input aka string into a list
user_distance = int(input_split[0]) #retrieving distance
user_metric = (input_split[1]) #retreiving metric

unit_converter(user_distance, user_metric) #calling function and passing the "split" user input

#Msc Code
#unit_converter(13, 'meters')
# print(input_values)
# print(user_distance)
# print(user_metric)
# print(type(user_distance))

