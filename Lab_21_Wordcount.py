import math
import string
import re
import requests


alpha = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!.?"


def count_letters(text):
    count = 0
    for letters in text:
        if letters.lower() in alpha:
            count += 1
    return count

def word_count(text):
    return len(text.split())


response = requests.get("https://www.gutenberg.org/files/60236/60236-0.txt")
book_text = response.text

words = word_count(book_text)
print(word_count(book_text))
