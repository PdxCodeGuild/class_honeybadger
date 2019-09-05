# practice_2_strings_prob7.py

# Convert input strings to lowercase without any surrounding whitespace.

def lower_no_white(a):
    result = a.strip()
    result = result.lower()
    return result

user_input = input("Please enter a phrase with uppercase and space before and after: ")

print(lower_no_white(user_input))