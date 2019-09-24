'''
Lab 2: Mad Libs

Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.
Instructions

    Search the interwebs for an example Mad Lib
    Ask the user for each word you'll put in your Mad Lib
    Use string concatenation to put each word into the Mad Lib

Example
>>> Give me an antonym for 'data': nonmaterial
>>> Tell me an adjective: Bearded
>>> Give me a sciency buzzword: half-stack
>>> A type of animal (plural): parrots
>>> Some Sciency thing: warp drive
>>> Another sciency thing: Trilithium crystals
>>> Sciency adjective: biochemical
...
>>> Nonmaterial Scientist Job Description:
>>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
>>> Key responsibilities:
>>> - Extract patterns from non-material
>>> - Optimize warp drive
>>> - Transform trilithium crystals into biochemical material.    


>>> - Birthday Madib:

My name is ________. (enter your name)
And I've known Dan for __________ years.               ----> (enter a number)
I am ________________ to be here                       ----> (enter and adjective)
to celeberate his/her _______ birthday.                    ----> (enter a number )
I can still remember when you were just ________ years old!        ----> enter a number
How time has flown by!  Remember that time when _____________ (memory here)     ----> enter a memory 
I always _____ whenever I think of all of that!        ----> enter a verb
Thank you for all of the wonderful memories. 
This year I hope you                                   -----> enter birthday wish 
Happy Birthday _________                               ----> enter name

'''
user_name = input('Please enter your name ')
birthday_name = input('Please enter the name of the person celebration their birthday ').upper()
number_years_known = int(input('Please enter a number '))
adjective = input('Please enter an adjective ')
birthday_age = int(input('Please enter a second number '))
young_age = int(input('Please enter a third number '))
memory = input('Please enter a brief memory ').upper()
verb = input('Please enter a verb ')
wish = input('Please enter a wish ').upper()

print()
print()

#Printing Madlib
print(f'My name is {user_name}. And Ive known {birthday_name} for {number_years_known} years.')
print(f'I am {adjective} to be here to celeberate {birthday_name}\'s {birthday_age} birthday')
print(f'I can still remember when {birthday_name} was just {young_age} years old!! How time has flown by!')
print(f'Remember that time when {memory}.')
print(f'I always {verb} whenever I think of all of that!')
print(f'Thank you for all of the wonderful memories.')
print(f'This year I hope you {wish}. ')
print(f'Happy Birthday {birthday_name}!')

print()
'''
Version 2 (optional)

Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, 
then use the .split() function to store each adjective and later use it in your story.

Add randomness! Use the random module, rather than selecting which adjective goes where in the story.

'''
def adjectives(user_input):
    user_split = user_input.split(',') #split puts values in a list. need to assign list to a variable in order to reference split list
    print(user_split)
    for i in range(len(user_split)):
        #print(i) #iterates over indicies and prints index
        #print(user_split[i]) # iterates over indicies and prints value at the index
        adj1 = user_split[0] 
        adj2 = user_split[1]
        adj3 = user_split[2]
    return adj1, adj2, adj3


user_input = input('Enter 3 adjectives seperated by commas ')
# user_split = user_input.split(',')
# print(user_input)
# print(user_split)

#Additional text to add.
new_adjectives = adjectives(user_input)
print(f'You can name your new triplets {new_adjectives[0]}, {new_adjectives[1]} and {new_adjectives[2]}.')




    
   









