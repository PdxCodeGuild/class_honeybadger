# practice_2_strings_prob6.py

# Return the number of letter occurances in a string.

def letter_word(a, b): 
    return b.count(a)

user_input_a = input("Please enter a single letter: ")
user_input_b = input("Please enter a phrase: ")
user_num = letter_word(user_input_a, user_input_b)

print(f"\nYou have {user_num} occurrences of {user_input_a} in your phrase.")