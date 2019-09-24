from turtle import *

def M():
    penup()
    setpos(-280,0)
    pendown()
    right(90)
    forward(100)
    penup()
    setpos(-280,0)
    left(45)
    pendown()
    forward(75)
    left(90)
    forward(75)
    right(135)
    forward(100)
    print(pos())


def A():
    penup()
    setpos(-169,-100)
    left(180)
    pendown()
    color('blue')
    forward(100)
    right(90)
    forward(75)
    right(90)
    forward(100)
    right(180)
    penup()
    forward(50)
    pendown()
    color('red')
    left(90)
    forward(75)
    penup()
    right(180)
    forward(75)
    right(90)
    forward(50)
    print(pos())

def T():
    penup()
    setpos(-50,-100)
    right(180)
    pendown()
    forward(100)
    left(90)
    forward(100)
    right(180)
    forward(150)
    right(90)
    penup()
    forward(100)
    right(180)
    pendown()
    forward(100)
    right(90)
    forward(50)


def T2():
    pass



M()
A()
T()

done()
exit()
