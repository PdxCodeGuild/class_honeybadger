# lab_06_password_generator.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab06-random_password.md

import random
import string

def password():
    password_dict = {
        1 : list(string.ascii_lowercase),
        2 : list(string.ascii_uppercase),
        3 : list(string.digits),
        4 : list(string.punctuation),
        }
    
    password = []

    length = input("How many characters would you like your password to be? ")
    length = int(length)
    while length > 0:
        step_1 = random.randint(1, len(password_dict))
        step_2 = random.choice(password_dict[step_1])
        password.append(step_2)
        length -= 1
        # step_2 = random.choice()
    
    random.shuffle(password)
    password = "".join(password)
    
    return print(password)
    
password()