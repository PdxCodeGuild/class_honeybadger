from turtle import *
#
# fillcolor('red')
# begin_fill()
# # body
# left(90)
# forward(90)
# forward(90)
#
# left(45)
# forward(45)
# right(45)
# forward(45)
# right(45)
# forward(45)
# right(45)
# forward(45)
# right(45)
# forward(45)
# right(45)
# forward(45)
# right(45)
# forward(45)
# left(45)
# forward(180)
# left(45)
# forward(90)
# right(180)
# forward(90)
# left(45)
# forward(45)
# left(45)
# forward(90)
# right(180)
# forward(90)
# left(45)
# forward(120)
# left(90)
# forward(90)
# right(180)
# forward(90)
# right(90)
# forward(120)
# left(90)
# forward(45)
#
# end_fill()
#
# left(90)
# forward(120)
# right(90)
# forward(90)
#
# # edge_length = 0
# # i = 0
# # while i < 100:
# # 	forward(edge_length)
# # 	right(144)
# #
# # 	edge_length += 4
#
# done()
#
# i = 0
# while i < 4:
#     forward(100)
#     left(90)
#     i = i + 1
#
# done()

fillcolor('pink')

n_sides = 12
edge_length = 0

i = 0
begin_fill()
while i < 150:
	forward(edge_length)
	right(360/n_sides)
	i = i + 1
	edge_length = edge_length + 1
end_fill()

# edge_length = 0
# i = 0
# while i < 100:
# 	forward(edge_length)
# 	right(144)
#
# 	edge_length += 4
done()
