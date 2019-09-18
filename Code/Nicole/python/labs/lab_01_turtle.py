# lab_01_turtle.py

# Use these functions to draw a stick figure with a head, body, two arms, and two legs.

import turtle as t
from random import randint

t.screensize(500,500)
t.speed(200)
# t.pensize(4)

# creates a never-ending colorful drawing of octagons stacked on top of each other

def hypnotic_octagon():
    while True:
        t.colormode(255)
        t.pencolor(randint(0,255),randint(0,255),randint(0,255))
        for i in range(8):
            t.forward(100)
            t.left(45)
        t.left(100.5)

    t.exitonclick()

# creates a never-ending colorful drawing of octagons with a gradient

def hypnotic_color_grade():
    while True:
        t.colormode(255)
        for i in range(0, 255):
            t.pencolor(i, 115, 125)
            for k in range(4):
                for j in range(8):
                    t.forward(100)
                    t.left(45)
                t.left(100.5)

    t.exitonclick()

def design():
    t.hideturtle()
    num = 100.0 # this is the length of each octagon side
    pen = 1.0 # this is the starting pen size
    while num > 0:
        t.colormode(255)
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

design()
