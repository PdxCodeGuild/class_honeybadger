# practice_2_strings_prob5.py

# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

# def cat_dog(a):
#     cat_number = a.count("cat")
#     dog_number = a.count("dog")
#     result = ""
#     if cat_number == dog_number:
#         result = True
#     else:
#         result = False
#     return result
    
# one-liner

def cat_dog(a):
    return a.count("cat") == a.count("dog")
        
    

print(cat_dog("cat cat cat dog dog dog dog cat dog"))