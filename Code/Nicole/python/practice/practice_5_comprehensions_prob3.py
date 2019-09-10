# practice_5_comprehensions_prob3.py

# Write a dictionary comprehension to swap keys and values of a given dictionary. 
# So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.

dictionary = {"a": 1, "b": 2, "c": 3}
print(dictionary)

def dict_swap(dict):
    return {v:k for k, v in dict.items()}

print(dict_swap(dictionary))