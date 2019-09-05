# practice_5_dicts_prob1.py

# Given a the two lists below, combine them into a dictionary.

def combine(list_1, list_2):
    return {list_1[x]:list_2[x] for x in range(len(list_1))}

def combine_zip(list_1, list_2):
    return dict(zip(list_1, list_2))

fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

print(combine(fruits, prices))
print(combine_zip(fruits, prices))