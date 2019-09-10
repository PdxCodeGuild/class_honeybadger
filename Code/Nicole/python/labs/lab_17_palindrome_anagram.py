# palindrome_anagram.py

# Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

def palindrome(word):
    return word == word[::-1]

user_word = input("Please type a word: ")

print(palindrome(user_word))