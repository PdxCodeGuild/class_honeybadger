# ''' Problem1: Get string from user, print out another string, doubling every letter'''

# Solution
# user_string = input('enter a string') 
# new_string = ''
# for i in range(len(user_string)):
#     new_string += 2*user_string[i]   #put in a new string 2x
# print(new_string)    

# '''
# Problem2:
# Write a function that takes a string, and returns a list of strings, 
# each missing a different character.
# '''
# #Solution
# import random
# def missing_chars(a_string, num_runs):
#     missing_strings = []
#     for i in range(num_runs):#limits number of times 
#         string = list(a_string) #converts string to list
#         string.pop(random.choice(range(len(a_string))))#getting length or astring, getting range, random choice randomly selects number from the range, pop removes this random number
#         new_string = '' #create new container to append
#         for i in range(len(string)): 
#             new_string += string[i]
#         missing_strings.append(new_string)
#     return(missing_strings)
# print(missing_chars('unicor',3))

# ###Alternative Solution#######
# def missing_char(a):
#     new_string = ''
#     index =0
#     for char in a: #iterates over charachter
#         new_string += a[:index]
#         index +=1
#         new_string += a[index:] + " "
#     return new_string.split(" ")

# user_input = input ("Please type a word: ")
# print(missing_char(user_input))

# '''
# Problem3:
# Return the letter that appears the latest in the english alphabet.
# '''
# def return_lastest(a_list):
#     a_list.sort() #sort list
#     return a_list[-1] #returns the last element

# print(return_lastest(list('antideprestentsljl'))) #calling module, converting the parameter to list 



# '''
# Problem4:
# Write a function that returns the number of occurances of 'hi' in a given string.

# '''
# #My Solution
# def hi(value):
#     count = 0
#     input = value
#     if 'hi' in input:
#         count +=1
#         print(count)
#     else:
#         #continue
#         print('not here')
#     return count
        
# hi('low')  

# #problem 4 - Judy's approach 
# phrase = input('phrase...')
# count = 0
# while 'hi' in phrase:
#     count +=1
#     phrase = phrase.replace('hi','',1)    
# print(count)

# '''
# Problem 5
# Write a function that returns True if a given string contains the same number 
# of 'cat' as it does 'dog'
# '''
# #Long approach 
# # user_input = (input('Please enter input'))
# # print(user_input)

# # def cat_dog():
# #     count_cats =0
# #     count_dogs =0
# #     if 'cat' in user_input:
# #         count_cats +=1
# #         print(count_cats)
    
# #     if 'dog' in user_input:
# #         count_dogs +=1
# #     print(count_dogs)

# #     if count_cats == count_dogs:
# #         print("True")
# #     else:
# #         print("False")

# # cat_dog()

# #Approach using count function 
# user_input = (input('Please enter input'))
# print(user_input)

# cat_counts = user_input.count('cat')
# print (cat_counts)
# dog_counts = user_input.count('dog')
# print(dog_counts)
# if cat_counts==dog_counts:
#     print('true')
# else:
#     print('false ')

'''
# Problem 6
# Return the number of letter occurances in a string.
# '''

# input = 'Hello. Happy Happy Friday'
# checking = 'H'

# counts = input.count(checking)
# print(counts)

'''
Problem 7
Convert input strings to lowercase w/o any surrounding whitespace.
'''

def lower():
    input = '           NANNANANANA BATMAN           '  
    print(input)
    input_lower = input.lower()
    print(input_lower)
    no_space = input_lower.strip()
    print(no_space)

lower()

# def count_hi(a_string)
# new_string = list(a_string)
# num_hi = 0
# for index in range(len(new_string)):
#     if new_string[index] == h and new_string[index+1] ==i:#index +1 moves to next position
#         num_hi +=1
#     continue
# return num_hi
# print(count_hi(###))


# #####    
# def missing_chars(a_string, num_runs = 3):
#     missing_strings = []
#     for i in range(num_runs):#limits number of times 
#         missing_strings.append(a_string.replace(random.choice(a_string), '' 1))
#     return missing_strings
# print(missing_chars('apple',6))   




