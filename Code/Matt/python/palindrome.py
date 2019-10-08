# user_word = input("Enter a word: ")
# def palindrome_checker(input):
#
#     if user_word == user_word [::-1]:
#         print(f'{user_word} is a Palindrome!')
#     else:
#         print(f'{user_word} is not a Palindrome!')
# palindrome_checker(user_word)
import string

user_first_word = input('Enter your first word: ').lower().replace(' ','')
user_second_word = input('Enter your second word: ').lower().replace(' ','')
first_word_sorted = ''.join(sorted(user_first_word))
second_word_sorted = ''.join(sorted(user_second_word))


# print(f'{first_word_sorted}&{second_word_sorted}')
if first_word_sorted == second_word_sorted:
    print(f'{user_first_word} & {user_second_word} are anagrams!')
else:
    print(f'{user_first_word} & {user_second_word} are not anagrams!')
