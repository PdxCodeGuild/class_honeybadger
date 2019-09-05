# Given a the two lists below, combine them into a dictionary.
# #
# def combine(a, b):
#     ...


# combine(fruits, prices) -> {'apple':1.2, 'banana':3.3, 'pear':2.1}
# from statistics import mean

# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]
# def combine (a,b):
#     return dict(zip(fruits,prices))
# combined_dict = combine(fruits,prices)
#
#
#
#
# def average(a_dict):
#     fruit_value = combined_dict.values()
#     fruit_price_list = list(fruit_value)
#     averaged_list = sum(fruit_price_list) / len(fruit_price_list)
#     print(averaged_list)
# average(combined_dict)
import string
# # generates a list of the alphabet
# alphabet = list(string.ascii_lowercase)
# # generates a dictionary with keys & values
# dictionary = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# # turns the dictionary into a list of the keys
# keys = str(dictionary.keys()))
# # keeps a total count of matches
# print(keys)
# # def average_numbers(a,b):
# #     total = 0
# #     for i in range(len(keys)):
# #         if str.startswith(keys, i ) == alphabet[i]:
# #             return total + 1
# #         else:
# #             # continue
# # print(average_numbers(alphabet , dictionary))

import string
# dictionary = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# dictionaryList = list(dictionary.keys())
# alphabet = string.ascii_lowercase
# print(dictionaryList)
# def unify(a_dict):
#     results = {}
#     for letter in alphabet:
#         count = 0
#         total = 0
#         for key in a_dict:
#             if not key.startswith(letter):
#                 continue
#
#             count += 1
#             total += dictionaryList[key]
#
#     return results
#
#
# unify(dictionaryList)
alpha = string.ascii_lowercase
dictionary = {}

def letter_to_ascii (a_string):
    return {i:ord(i) for i in alpha}

x = letter_to_ascii(alpha)
print(x)
