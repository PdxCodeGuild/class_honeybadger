# password generator

import random
import string

# variables

number = string.digits
letter_lower = string.ascii_lowercase
letter_upper = string.ascii_uppercase
char = string.punctuation

password = ""

# Determines number strings

len_number = input("How many numbers do you want in your password? ")
len_number = int(len_number)

for x in range(len_number):
    password += random.choice(number)

# Determines lowercase letter strings

len_letter_lower = input("How many lowercase letters do you want in your password? ")
len_letter_lower = int(len_letter_lower)

for x in range(len_letter_lower):
    password += random.choice(letter_lower)

# Determins uppercase letter strings

len_letter_upper = input("How many uppercase letters do you want in your password? ")
len_letter_upper = int(len_letter_upper)

for x in range(len_letter_upper):
    password += random.choice(letter_upper)

# Determines character strings

len_char = input("How many symbols/characters do you want in your password? ")
len_char = int(len_char)

for x in range(len_char):
    password += random.choice(char)

# password = random.shuffle(password)
password = list(password)
random.shuffle(password)
# s = ""
password = ("".join(password))


print(f"\nYour password is {password}\n")
