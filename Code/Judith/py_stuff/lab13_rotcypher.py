#filename: lab13_rotcipher.py

import string

alp = string.ascii_lowercase*2

def phr_check(phrase):
    check_phr = list(phrase)
    for let in check_phr:
        if let not in alp:
            return False
        else:
            continue
    return True

def rot():
    modphrase = ''
    for let in phrase:
        if let == ' ':
            modphrase += let
        else:
            modphrase += alp[alp.find(let) + deg%26]
    print(modphrase)

while True:
    phrase = input('give a phrase for rotation...')
    if phr_check(phrase):
        break
    else:
        print('invalid entry')
        continue


while True:
    deg = input('give a degree of rotation...')
    try:
        int(deg)
    except:
        print('invalid entry')
        continue
    deg = int(deg)
    break


rot()