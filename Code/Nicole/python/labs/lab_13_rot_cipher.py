# rot_cipher.py

# Write a program that prompts the user for a string, and encodes it with ROT13.
# For each character, find the corresponding character, add it to an output string.
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.

import string

# define function

# def enum(a_list):
#     return list(enumerate(a_list))
# 
# my_test_list = ["Nicole", "Angie", "Jodi"]
# 
# print("* " * 10)
# print(enum(my_test_list))
# print(len(my_test_list))
# print(my_test_list[2])
# print("* " * 10)


# def rot13(word, number):
#     alpha = list(string.ascii_lowercase)
#     cipher = []
#     for index, x in list(enumerate(alpha)):
#         print(f"Printing x {x}, index {index}")
#         for y in list(word):
#             print(f"Printing y {y}")
#             if x == y:
#                 # cipher.append((alpha[index + number - (len(alpha))]))
#                 cipher.append(alpha[(index + number) % 26])
#     result = "".join(cipher)
#     return result

# def rot13(word, number):
#     alpha = list(enumerate(string.ascii_lowercase))
#     cipher = []
#     calc = [cipher.append([x + number]) for index, x in alpha if x in word]
#     return cipher
#     # give me CIPHER LETTER 
    
# marina's solution:

alpha = string.ascii_lowercase*2 

def rot13(word, number):
   cipher = ""
   for x in word:
       if x == " ":
           cipher += x
       cipher += alpha[alpha.find(x) + (number % 26)]
   return cipher


user_word = input("\nWhat would you like to encrypt?\n")
user_number = input("What rotation would you like to use? Please enter a number:  ")
user_number = int(user_number)

print(rot13(user_word, user_number))