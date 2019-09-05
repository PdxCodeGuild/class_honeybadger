# user_string = input("please enter a word: ")
# new_str = ''
# for i in range(len(user_string)):
#     new_str += 2*user_string[i]
# print (new_str)

# def double_letters (a_string):
#     new_str = ''
#     for char in a_string:
#         double = char * 2
#         new_str += double
#     return new_str
# print(double_letters(input("please enter a word: ")))


# import random
#
# def missing_chars(a_string, num_runs = 3):
#     missing_strings = []
#     for i in range(num_runs):
#         missing_strings.append(a_string.replace(random.choice(a_string), '', 1))
#         # string = list(a_string)
#         # string.pop(random.choice(range(len(a_string))))
#         # new_string = ''
#         # for i in range(len(string)):
#         #     new_string += string[i]
#         # missing_strings.append(new_string)
#     return missing_strings
#
# print(missing_chars('apple', 6))


#
# def find_letter(a_string):
#     a_string.sort()
#     print(a_string)
#     return a_string[-1]
# user_input = list(input("give me a string: "))
#
# print(find_letter(user_input))

def count_hi(a_string, sub_string):

    print(a_string)
    # return(a_string)
    print(a_string.count(sub_string))
a_string = 'hihi'
sub_string = 'hi'
count_hi(a_string, sub_string)
