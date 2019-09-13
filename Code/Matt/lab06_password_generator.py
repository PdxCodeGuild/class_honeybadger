import random
import string

print('Welcome to password generator!')


alphabet = list(string.ascii_lowercase)


number_of_chars = int(input('How many characters do you want in your password?: '))

def pw_gen(list):
    password = ''
    for i in range(0,number_of_chars):
        password  += random.choice(alphabet)
    print(f'Your password is: {password}')
pw_gen(alphabet)
