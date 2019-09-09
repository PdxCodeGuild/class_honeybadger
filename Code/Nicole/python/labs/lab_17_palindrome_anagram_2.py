# palindrome_anagram_2.py

# Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

# X 1 - Convert each word to lower case (lower)
# X 2 - Remove all the spaces from each word (replace)
# 3 - Sort the letters of each word (sorted)
# 4 - Check if the two are equal

def anagram(word_1, word_2):
    return sorted(word_1) == sorted(word_2)

user_word_1 = input("Please enter a word or sentence: ").lower()
user_word_1 = user_word_1.replace(" ", "")
user_word_2 = input("Please enter another word or sentence: ").lower()
user_word_2 = user_word_2.replace(" ", "")

print(anagram(user_word_1, user_word_2))