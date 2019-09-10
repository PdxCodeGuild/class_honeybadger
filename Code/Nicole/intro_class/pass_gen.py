# password generator

import random
import string

# variables

number = string.digits
letter_lower = string.ascii_lowercase
letter_upper = string.ascii_uppercase
char = string.punctuation

pass_combine = number + letter_lower + letter_upper + char

length = input("How long would you like your password to be? ")
length = int(length)

password = ""
for x in range(length):
    password += random.choice(pass_combine)

print(f"\nYour password is {password}\n")
