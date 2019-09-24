'''
Lab 6: Password Generator

Let's generate a password of length n using a while loop and random.choice, this will be a 
string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of 
a list.

Concepts Covered

    input, print
    looping
    random.choice
    the 'sting builder pattern'
'''

import random
#Approach 1********************************************************************************************
# def random_char(number):
#     num = 0
#     mylist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
#     while num <number:
#         random_letter = random.choice(mylist)
#         print(random_letter, end=(' '))
#         num+=1
#     return

# user_input = int(input('Please enter a number '))
# print('Your new password is:')
# random_char(user_input)

#Approach 2********************************************************************************************

def random_char2(user_input):
    password = []
    #print(user_input)
    split_values = user_input.split(',') #splits puts variables in a list but need a new variable to see list
    #print(split_values)
    for i in split_values:
        #print(i)
        upper = split_values[0].upper()
        lower = split_values[1].lower()
        number = (split_values[2])
        special = split_values[3]
    #print(upper, lower, number, special, end=' ')
    password.append(upper)
    password.append(lower)
    password.append(number)
    password.append(special)
    #print(password)
    print(",".join(password))

    # for p in password:
    #     print ('-'.join(p) )
    # print(password)
        
    

        
    #break apart the input into 4 variables, uppercasing and lowercasing the 1st 2 variables 
    #join them


user_input2 = input('Enter a capital and lowercase letter, number and special charachter seperated by commas ')
random_char2(user_input2)
#ask user for a capital letter, lowercase letter, number and special charachter
#append these to a single list and use .join to put it all together



