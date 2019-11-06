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
        }
     
    password = ""
    
    for key in password_dict:
        length = 3
        password += password_part(length, password_dict[key])
    
    password = list(password)
    # print(password)
    random.shuffle(password)
    # print(password)
    password = "".join(password)
    # print(password)
    
    return password
    