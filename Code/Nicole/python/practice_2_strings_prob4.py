# practice_2_strings_prob4.py

# Write a function that returns the number of occurances of 'hi' in a given string.

# define the function

# def count_hi(a):
#     hi_number = (len(a))/2
#     return hi_number
    
def count_hi_2(a):
    hi_number = a.count("hi")
    return hi_number

print(count_hi_2("hihihi hi hi hhhiiii people"))