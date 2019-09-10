# power_list = [1,2,3,4,5,6,7,8,9,10]
# def power(my_list):
#     return [ x**2 for x in my_list ]
# print(power(power_list))
# for i in range(10):
#     print(2 ** i)
# print([2 ** i for i in range(10)])


#  Write a comprehension to generate the first 10 even numbers.
#
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# def even_number():
#     return  [ x for x in range(20) if x % 2 == 0]
# print(even_number())

# Write a dictionary comprehension to swap keys and values of a given dictionary. So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.
dict_1 = {'a': 1, 'b': 2}

for x,y in dict_1.items():
