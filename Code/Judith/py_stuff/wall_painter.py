#filename: wall-painter.py

import math

print("We're going to calculate the cost to paint a wall.../n")

#define Variables from user input

room_h=float(input("Enter the height of the room..."))
room_w=float(input("Enter the width of the room..."))
coatnum=float(input("how many coats would you apply?.."))
pcost=float(input("How much does a gallon of your chosen paint cost?.."))


#one gallon of paint is assumed to cover 400 sq ft
cov=400

#calculate sq ft of wall
wallsqft=room_h*room_w

#multiply by number of coats
totalsqft=float(wallsqft*coatnum)

#total gallons
totalgal=math.ceil(totalsqft/cov)

totalcost=totalgal*pcost

print("The total cost to paint the wall is ",totalcost," dollars")
