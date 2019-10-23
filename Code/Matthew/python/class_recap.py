
import math

def is_power_of_3(n):
    if n == 0:
        return False
    x = math.log(n, 3)
    print(x)
    if abs(x - round(x)) < 0.00001:
        return True
    return False

inputs = [(27, True),
          (28, False),
          (59049, True),
          (0, False),
          (1, True),
          (177146, False)]
for input in inputs:
    if is_power_of_3(input[0]) != input[1]:
        print(f'ERROR with input {input[0]}')
    else:
        print('passed')




# class Animal:
#     def __init__(self, name, age=10):
#         self.name = name
#         self.age = age
# 
#     def __lt__(self, other):
#         return self.age < other.age
# 
#     def __str__(self):
#         return f'My name is {self.name}, my age is {self.age}'
# 
# animal1 = Animal('mike')
# animal2 = Animal('jill', 20)
# 
# print(animal1 < animal2)