# lab_06_password_generator_v2.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab06-random_password.md

import random
import string


def password_part(n_chars, characters):    
    passwordy = ""
    
    while n_chars > 0:
        password_update = random.choice(characters)
        passwordy += password_update
        n_chars -= 1
    
    return passwordy


def password():   
    password_dict = {
        "lowercase" : list(string.ascii_lowercase),
        "uppercase" : list(string.ascii_uppercase),
        "number" : list(string.digits),
        "special" : list(string.punctuation),
        }
     
    password = ""
    
    for key in password_dict:
        length = input(f"How many {key} characters would you like your password to have?\n")
        length = int(length)
        password += password_part(length, password_dict[key])
        print(f"Test: {password}")
    
    password = list(password)
    print(password)
    random.shuffle(password)
    print(password)
    password = "".join(password)
    print(password)
    
    # return print(password)
    
password()