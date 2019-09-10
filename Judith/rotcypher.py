#filename: rotcipher.py

import string

alp = string.ascii_lowercase*2

phrase = input('give a phrase for rotation...')
deg = int(input('give a degree of rotation...'))

def rot():
    modphrase = ''
    for let in phrase:
        if let == ' ':
            modphrase += let
        modphrase += alp[alp.find(let) + deg%26]
    print(modphrase)

rot()