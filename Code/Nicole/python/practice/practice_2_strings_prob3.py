# practice_2_strings_prob3.py

# Return the letter that appears the latest in the english alphabet.

import string

# define function

def return_latest(a):
    alpha = string.ascii_lowercase
    index = 0
    final_letter = ""
    for char in alpha:
        index -= 1
        # subtracts 1 from the index value for each loop.
        last_letter = alpha[index] 
        # Converts the alphabet index into a letter, should start with z and go backwards
        if a[a.find(last_letter)] in last_letter:
            final_letter += a[a.find(last_letter)]
            break
            # checks to see if the last letter in the alphabet is in the user's input. Continues through this loop. If it is true, it breaks the loop.
            # a.find returns an index value, so I converted it with the a[] to return a string (not an integer)
    return final_letter
    
user_input = input("Please type a string of letters: ")

print(return_latest(user_input))