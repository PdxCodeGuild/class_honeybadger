# practice_5_dicts_prob3.py

# Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.

# d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# unify(d) -> {'a':3, 'b':4, 'c':5}

import string

# def same_letter(dict):
#     alpha = string.ascii_lowercase
#     new_dict = {}
#     for x in alpha:
#         count = 0
#         avg_list = []
#         avg = 0
#         new_keys = []
#         for key in dict:
#             # if x in dict.keys() == dict.key().startswith(x):
#             if key.startswith(x):
#                 count += 1
#                 avg_list.append(dict.value())
#                 avg = sum(avg_list) / count
#         new_dict.update({x: avg})
#     return new_dict

def same_letter(dict):
    alpha = string.ascii_lowercase
    new_dict = {}
    for x in alpha:
        count = 0
        avg_list = []
        avg = 0
        for key in dict:
            if not key.startswith(x):
                continue
            count += 1
            avg_list.append(dict[key])
            avg = sum(avg_list) / count
            new_dict.update({x: avg})
    return new_dict


my_dict = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6, 'apple': 7, 'grape': 12, 'gorilla': 2}

print(same_letter(my_dict))