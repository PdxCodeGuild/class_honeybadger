

import random
import string




# #           0          1          2          3
# fruits = ['apples', 'bananas', 'avocado', 'tomato']
# 
# # no - does not work
# fruit = fruits[0]
# fruit = 'pear'
# print(fruits[0])
# 
# # yes - does work
# fruits[0] = 'pear'
# 
# 
# s2 = ''
# for fruit in fruits:
#     s2 += fruit + ' '
# 
# print(s2)
# exit()


# for i in range(10)
# for i in range(len(fruits))


class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y
        
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)



p = Point(5, 2) # call the initializer, instantiate the class
print(p.x) # 5
print(p.y) # 2

c = Point(10, 5)

d = p.distance(c)




print(type(p)) # Point




def random_password(n_lower, n_upper, n_number, n_special):
    # password = []
    # password.extend([random.choice(string.ascii_lowercase) for i in range(n_lower)])
    password = ''
    for i in range(n_lower):
        print(password)
        password += random.choice(string.ascii_lowercase)
    for i in range(n_upper):
        print(password)
        password += random.choice(string.ascii_uppercase)
    for i in range(n_number):
        print(password)
        password += random.choice(string.digits)
    for i in range(n_special):
        print(password)
        password += random.choice(string.punctuation)
    
    password = list(password)
    random.shuffle(password)
    return ''.join(password)

print(random_password(3, 3, 3, 3))














