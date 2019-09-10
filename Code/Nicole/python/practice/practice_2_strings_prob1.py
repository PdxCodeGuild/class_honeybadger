# practice_2_strings_prob1.py

def double_every_letter(a):
    new_string = ""
    for char in a:
        double = char * 2
        new_string += double
    return new_string

user_input = input("Please enter some text: ")

print(double_every_letter(user_input))