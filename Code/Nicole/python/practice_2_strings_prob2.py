# practice_2_strings_prob2.py

# Write a function that takes a string, 
# and returns a list of strings, 
# each missing a different character.

# define function

def missing_char(a):
    new_string = ""
    index = 0
    for char in a:
        new_string += a[:index]
        index += 1
        new_string += a[index:] + " "
    return new_string.split(" ")

user_input = input("Please type a word: ")

print(missing_char(user_input))