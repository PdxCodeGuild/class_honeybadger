# Password Generator

# variables

import random
import string

print("Welcome to Random Password!")

choices = string.digits + string.ascii_lowercase + string.punctuation + string.ascii_uppercase

user_input = int(input("How long would you like your password to be? "))

def randomString(stringLength=user_input):
    return ''.join(random.choice(choices) for i in range(stringLength))

print ("Password is ", randomString() )
