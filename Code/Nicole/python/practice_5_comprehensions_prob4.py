# practice_5_comprehensions_prob4.py

# Write a dictionary comprehension to print each letter of the alphabet and its corresponding ASCII code

import string

# for char in string.ascii_lowercase:
#     print(ord(char))

def convert_to_ascii():
    return {char: ord(char) for char in string.ascii_lowercase}

# dict_variable = {key:value for (key,value) in dictonary.items()}


print(convert_to_ascii())