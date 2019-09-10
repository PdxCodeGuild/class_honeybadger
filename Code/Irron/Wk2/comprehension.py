####Comprehension Practice ######################
'''
Prob1
Write a comprehension to generate the first 10 powers of two.

'''
# def powers_of_two(num_powers):
#     return[2 ** num for num in range(num_powers)] #for number in this range num_powers, 
#                     #take 2 and raise it to that number. After you do this, put in list

# print([powers_of_two(10)])

'''
Prob2
Write a comprehension to generate the first 10 even numbers.
'''

# def gen_even():
#     return [number for number in range(20) if number %2 == 0] # for number in range 20
#                                                               #if that number is even
#                                                               #return number

# print(gen_even) #call module

'''
Prob3
Write a dictionary comprehension to swap keys and values of a given dictionary. 
So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.
'''
#example of how to loop through dictionary 
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k,v in knights.items():
#     print(k, v)

# def dict_swap(a_dict):
#     return {value: key for key, value in a_dict.items()}

# some_dictionary = {'a':1, 'b':2}
# print(dict_swap(some_dictionary))


################Dictionary Practice####################
'''
Prob1
Given a the two lists below, combine them into a dictionary.

def combine(a, b):
    ...
fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
combine(fruits, prices) -> {'apple':1.2, 'banana':3.3, 'pear':2.1}

'''
####Verbose way - Justing approach ####
# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]

# def combine_lists(list_1, list_2):
#     combined = {}
#     for i in range(len(list_1)):
#         combined.update({list_1[i] : list_2[i]})
#     return combined
# print(combine_lists(fruits, prices))

##Using zip function #####
# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]

# def combine_lists(list_1, list_2):
#     return dict(zip(fruits, prices))

# fruit_prices = combine_lists(fruits, prices)
# print(fruit_prices)

'''
Prob2
Using the result from the previous problem, iterate through the dictionary and 
calculate the average price of an item.

def average(d):
    ...
combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
average(combined) -> 2.2

'''
# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]

# def combine_lists(list_1, list_2):
#     return dict(zip(fruits, prices))

# fruit_prices = combine_lists(fruits, prices)
#print(fruit_prices)

#Solution 
# def calc_average_price(a_dict):
#    prices = list(a_dict.values()) #creates a list of the prices based on prices list
#    total = 0
#    for price in prices:
#         total += price #keeping a running total of prices
#    return round(total /len(prices)) #computing the average

# print('The average is:')
# print(calc_average_price(fruit_prices)) #printing average price 

'''
P3
Average numbers whose keys start with the same letter. Output a dictionary containing
those letters as keys and the averages.

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
unify(d) -> {'a':3, 'b':4, 'c':5}

'''
import string
alphabet = string.ascii_lowercase #imports alphabet in lower case
#print(alphabet)

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
#iterate thru the alphabet beginning with a 
#compare a (this positon) to the first position of key in the dictionary. if its a match, add the value
# for i in range(len(alphabet)):
#     print(i, end=" ") #this prints the index

# for a,b in enumerate(alphabet):
#     print(f'{a} {b}') #this creates 2 colums one for the index and other for its respecitve value 

#iterate thru the alphabet
for char in alphabet:
    print(char)

# for key in d:
#     print(key)

#steps: compare the alphabet to the first letter of the key. if match count






