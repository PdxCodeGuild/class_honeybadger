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


def password(num_lowercase, num_uppercase, num_number, num_special):   
    password_dict = {
        "lowercase" : list(string.ascii_lowercase),
        "uppercase" : list(string.ascii_uppercase),
        "number" : list(string.digits),
        "special" : list(string.punctuation),
        }
     
    password = ""
    
    
    index = 0
    mynums = [num_lowercase, num_uppercase, num_number, num_special]
    for key in password_dict:
        length = mynums[index]
        password += password_part(length, password_dict[key])
        index += 1
    
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    return password
    
    # return print(password)
    