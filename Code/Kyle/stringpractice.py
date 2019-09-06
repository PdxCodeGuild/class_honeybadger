# import random
#
# def missing_chars(a_string, num_runs):
#     missing_string = []
#     for i in range(num_runs):
#         string = list(a_string)
#         string.pop(random.choice(range(len(a_string))))
#         new_string = ''
#         for i in range(len(string)):
#             new_string += string[i]
#         missing_string.append(new_string)
#     return missing_string
#
# print(missing_chars('volcano', 6))

def missing_chars(a_string, num_runs):
    missing_string = []
    for i in range(num_runs):
        missing.append(a_string.replace(random.choice(a_string), '', 1))
    return missing_string

print(missing_chars('apple', 6))
