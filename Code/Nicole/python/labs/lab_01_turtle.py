# lab_01_turtle.py

# Use these functions to draw a stick figure with a head, body, two arms, and two legs.

import turtle as t
from random import randint

t.screensize(5120,2880)
t.colormode(255)
# t.bgcolor(230, 230, 230)
t.speed(0)
t.pensize(4)

# creates a never-ending colorful drawing of octagons stacked on top of each other

def hypnotic_octagon():
    t.title("Hypnotic octagon")
    while True:
        t.pencolor(randint(0,255),randint(0,255),randint(0,255))
        for i in range(8):
            t.forward(100)
            t.left(45)
        t.left(100.5)

    t.exitonclick()

# creates a never-ending colorful drawing of octagons with a gradient

def hypnotic_color_grade():
    t.title("Gradient octagon")
    while True:
        for i in range(0, 255):
            t.pencolor(i, 115, 125)
            for k in range(4):
                for j in range(8):
                    t.forward(100)
                    t.left(45)
                t.left(100.5)

    t.exitonclick()

# changes the pen size throughout the loop

def change_pen_size():
    t.title("Changing pen size")
    t.hideturtle()
    num = 100.0 # this is the length of each octagon side
    pen = 1.0 # this is the starting pen size
    while num > 0:
        for i in range(0, 255):
            t.pencolor(i, i, 182) # i changes which makes a gradient
            t.pensize(pen) # determines pen size
            for j in range(8): # makes an octagon
                t.forward(num)
                t.left(45)
            t.left(100.5) # rotates to the left
            num -= 0.1 # decreases the size of the octagon until it hits zero
            pen += 0.01 # makes the pen size smaller

    t.exitonclick()

# makes a spiral with random colors each time it's run

def color_spiral():
    t.title("Octagon spiral with random colors")
    t.hideturtle()
    num = 100.0 # this is the length of each octagon side
    pen = 4.0 # this is the starting pen size
    x = randint(0, 255)
    y = randint(0, 255)
    while num > 0:
        for i in range(0, 255):
            # x = randint(0,255)
            t.pencolor(i, (x%255), (y%255)) # i changes which makes a gradient
            # t.pensize(pen) # determines pen size
            for j in range(8): # makes an octagon
                t.forward(num)
                t.left(45)
            t.left(100.5) # rotates to the left
            num -= 0.1 # decreases the size of the octagon until it hits zero
            pen -= 0.001 # makes the pen size smaller
            x += 10 # this increments the g and b colors to make the spiral colors

    t.exitonclick()
    
def choose_sides():
    t.hideturtle()
    sides = t.numinput("Create your design:", "How many sides do you want the shape to have?")
    sides = int(sides)
    t.title(f"{sides}-sided design")
    num = 200.0 # this is the length of each side
    pen = 4.0 # this is the starting pen size
    x = randint(0, 255)
    y = randint(0, 255)
    while num > 0:
        for i in range(0, 255):
            t.pencolor(i, (x%255), (y%255)) # i changes which makes a gradient
            t.pensize(pen) # determines pen size
            for j in range(sides): # makes a shape
                t.forward(num + sides)
                t.left(360 / sides)
            t.left(100.5) # rotates to the left
            num -= 0.1 # decreases the size of the shape until it hits zero
            pen -= 0.001 # makes the pen size smaller
            x += 10 # this increments the g and b colors to make the spiral colors

    t.exitonclick()

def circle_spiral():
    t.title("Circle Spiral")
    t.hideturtle()
    num = 150.0 # this is the radius of the circle
    pen = 3 # this is the starting pen size
    x = randint(0, 255)
    y = randint(0, 255)
    while num > 0:
        for i in range(0, 255):
            # x = randint(0,255)
            i = (i+100)%255
            t.pencolor(i, (x%255), (y%255)) # i changes which makes a gradient
            t.pensize(pen) # determines pen size
            for j in range(3): # prints the circle four times
                t.circle(num)
                t.left(120)
            t.left(100.5) # rotates to the left
            num -= .25 # decreases the size of the circle until it hits zero
            pen -= 0.01 # makes the pen size smaller
            if pen <= .10:
                pen = .1
            x += 10 # this increments the g and b colors to make the spiral colors

    t.exitonclick()

def choose_program():
    user_input = t.textinput("Choose your program", "Which program do you want to run? \n    Type '1' for Hypnotic Octagon\n    Type '2' for Hypnotic Color Grade\n    Type '3' for Change Pen Size\n    Type '4' for Color Spiral\n    Type '5' for Choose Sides\n    Type '6' for Circle Spiral").lower()
    if user_input == "1":
        hypnotic_octagon()
    elif user_input == "2":
        hypnotic_color_grade()
    elif user_input == "3":
        change_pen_size()
    elif user_input == "4":
        color_spiral()
    elif user_input == "5":
        choose_sides()
    elif user_input == "6":
        circle_spiral()
        
        

choose_program()