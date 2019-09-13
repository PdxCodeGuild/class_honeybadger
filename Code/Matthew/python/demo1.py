
import random

x = 'mykey'
d = {x: 5}
print(d)


y = ['apples', 'bananas', 'pears']
d = {1: y}


fruits = ['apple', 'banana']
fruit_random = random.choice(fruits)
d = {'f': fruit_random}




d = {
    'random_fruit': lambda: random.choice(fruits)
}
for i in range(10):
    print(d['random_fruit']())
    






