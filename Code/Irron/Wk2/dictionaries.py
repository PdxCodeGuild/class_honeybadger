
'''
Prob1
Given a the two lists below, combine them into a dictionary.

def combine(a, b):
    ...
fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
combine(fruits, prices) -> {'apple':1.2, 'banana':3.3, 'pear':2.1}

'''
###Verbose way - Justing approach ####
fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

def combine_lists(list_1, list_2):
    combined = {}
    for i in range(len(list_1)):
        combined.update({list_1[i] : list_2[i]})
    return combined
print(combine_lists(fruits, prices))

###Using zip function #####
fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

def combine_lists(list_1, list_2):
    return dict(zip(fruits, prices))

fruit_prices = combine_lists(fruits, prices)
print(fruit_prices)


# '''
# Prob2
# Using the result from the previous problem, iterate through the dictionary and 
# calculate the average price of an item.

# def average(d):
#     ...
# combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
# average(combined) -> 2.2

# '''
# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]

# def combine_lists(list_1, list_2):
#     return dict(zip(fruits, prices))

# fruit_prices = combine_lists(fruits, prices)
# print(fruit_prices)

# Solution 
# def calc_average_price(a_dict):
#    prices = list(a_dict.values()) #creates a list of the prices based on prices list
#    total = 0
#    for price in prices:
#         total += price #keeping a running total of prices
#    return round(total /len(prices)) #computing the average

# print('The average is:')
# print(calc_average_price(fruit_prices)) #printing average price 


# '''
# Prob3
# Average numbers whose keys start with the same letter. Output a dictionary containing
# those letters as keys and the averages.

# d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# unify(d) -> {'a':3, 'b':4, 'c':5}

# '''
# import string
# alphabet = string.ascii_lowercase #imports alphabet in lower case
# #print(alphabet)

# d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# ##iterate thru the alphabet beginning with a 
# ##compare a (this positon) to the first position of key in the dictionary. if its a match, add the value
# for i in range(len(alphabet)):
#     print(i, end=" ") #this prints the index

# for a,b in enumerate(alphabet):
#     print(f'{a} {b}') #this creates 2 colums one for the index and other for its respecitve value 

# ##iterate thru the alphabet
# for char in alphabet:
#     print(char)

# for key in d:
#    print(key[0]) # this prints the first position of the key

# ##hold letter in alphabet constant and compares the letter to the dictionary. #
# ##The nested loop iterates the keys of the dictionary  
# def unify(a_dict):
#     results = {}
#     for letter in string.ascii_lowercase: #letter begins at letter a iterates through alphabet 
#         count = 0
#         total = 0
#         for key in a_dict: #isolates the keys in the dictionary, ie a1, a2, a3
#             if not key.startswith(letter): #saying if the letter of the alphabet does not begin with the beginning letter of key?
#                 continue
#             count +=1     #if stating at letter a, this counts the number of times a has been identifed/matched 
#             total+= a_dict[key] #using the key to get the value.  associates the matched values and totals the values
#             results.update({letter: round(total/count)})

#     return results

# print(unify(d))


# '''
# Prob4
# Write a dictionary comprehension to print each letter of the alphabet and its correstponding ASCII code (check out ord)

# {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, ...}

# '''
# import string
# # for char in string.ascii_lowercase:
# #     print({char: ord(char)})


# alpha = string.ascii_lowercase
# print({char: ord(char) for char in alpha})
