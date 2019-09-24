'''
Turtle is a python module that allows us to move a virtual turtle around the screen using 
programming statements. This turtle has a position and a heading. Below are a list of commands, 
you can more in the turtle docs.

    forward(distance) moves the turtle forward the given number of pixels

    left(angle) and right(angle) turns the turtle left or right by the given angle (in degrees)

    color(color_name) sets the pen's color, which can be penup() penup() penup()

    penup() raises the pen, a line won't be drawn when the turtle moves, pendown() lowers the pen 
    again

    setposition(x, y) moves the turtle to the given position

    fillcolor(color_name) sets the fill color, begin_fill() indicates you'd like to begin filling 
    in whatever you draw, end_fill() actually fills the shape in.

Use these functions to draw a stick figure with a head, body, two arms, and two legs. Once you're 
done, go through the examples below and create your own drawing.

'''
import turtle as t

''' Drawing A Circle '''
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# t.done

'''  Drawing A Square '''
# t.fillcolor('red')
# t.begin_fill()

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# t.end_fill()
# t.done

'''  Drawing A Star '''
# t.forward(100)
# t.right(144)
# t.forward(100)
# t.right(144)
# t.forward(100)
# t.right(144)
# t.forward(100)
# t.right(144)
# t. forward(100)

# t.done()

'''  Drawing A Square Loop '''
# i = 0
# while i < 4:
#     t.forward(100)
#     t.left(90)
#     i = i + 1

# t.done()


'''  Drawing A Staircase '''
# i = 0
# while i < 4:    
# 	t.forward(100)
# 	t.left(90)
# 	t.forward(100)
# 	t.right(90)
# 	i = i + 1
# t. done()

'''  Filling In A Square '''
# t.fillcolor('red')
# t.begin_fill()

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# t.end_fill()

# t.done()

''' Drawing an N sided figure '''
# t.edge_length = 100
# n_sides = 5

# i = 0
# while i < n_sides:
# 	t.forward(t.edge_length/n_sides)
# 	t.right(360/n_sides)
# 	i = i + 1

# t.done()


''' Drawing a 8 sided spiral '''
# t.fillcolor('blue')

# n_sides = 8
# t.edge_length = 0

# i = 0
# t.begin_fill()
# while i < 150:
# 	t.forward(t.edge_length)
# 	t.right(360/n_sides)
# 	i = i + 1
# 	t.edge_length = t.edge_length + 1
# t.end_fill()
# t.done()


# ''' Drawing a expanded star '''

t.edge_length = 0
i = 0
while i < 100:
	t.forward(t.edge_length)
	t.right(144)

	t.edge_length += 4

t.done()