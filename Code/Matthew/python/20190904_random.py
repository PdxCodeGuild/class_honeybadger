


def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total



# print(add(5, 2, 6, 7, 8, 9))


# def demo(*args, **kwargs):
#     print(args)
# 
# # list = ['hello', 'world', 'this', 'that']
# # dict = {
# #     'sep':' ',
# #     'end':'!!!!!!!!!!',
# # }
# 
# demo('hello', 'world', 'this', 'that')
# demo(*['hello', 'world', 'this', 'that'])

# words = ['hello', 'world', 'this', 'that']
# print(*words, sep='_')
# print('_'.join(words))



# list comprehensions
values = []
for i in range(10):
    values.append(i**2)
print(values)

values = [i**2 for i in range(10)]
print(values)

# concatenating a list of lists of strings
xs = [['x', 'x', 'x'], ['x', 'x'], ['x']]

for x in xs:
    print(' '.join(x))

print(' '.join(xs))

print([' '.join(x) for x in xs])
print(xs)
print('\n'.join(['_'.join(x) for x in xs]))

print('x_x_x'.split('_'))










#           0         1           2          3          4          5
fruits = ['apples', 'bananas', 'pears', 'cherries', 'avocados', 'tomatoes']


prices = {
    'apples': 1.0,
    'bananas': 0.8,
    'pears': 0.5,
    'avocados': 0.8
}



print(list(prices.keys()))
print(prices.values())
print(prices.items()) # prices = [('apples', 1.0), ('bananas', 0.8)]
print(prices)


for key in prices:
    if prices[key] == 0.8:
        print(key)
        break

# for key in prices:
#     print(key, prices[key])



# iterate over the indices
# for i in range(len(fruits)):
#     print(i, fruits[i])

# iterate over the elements
# for fruit in fruits:
#     print(fruit)



# for char in 'hello world!':
#     print(char)

# for fruit in reversed(fruits):
#     print(fruit)


# for i in range(len(fruits)-1, -1, -1):
#     print(fruits[i])



# for i in range(len(fruits)*2-1, -1, -1):
#     print(fruits[i//2])

# for i in range(10): # 0 -> 9
# for i in range(5, 10) # % 5 -> 9

# for i in range(10, 5, -1): # 10, 9, 8, 7, 6
#     print(i)
 















