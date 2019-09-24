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

def sentance_counter(text):
    count = 0
    for i in text:
        if i in punctuation:
            count +=1
    return count


def ari(text):
    ari = 4.71*(chars / words) + 0.5*(words / punct) -21.43
    ari = round(ari)
    if ari > 14:
        ari = 14
    return ari


response = requests.get("https://www.gutenberg.org/files/60236/60236-0.txt")
book_text = response.text
chars = count_letters(book_text)
words = word_count(book_text)
punct = sentance_counter(book_text)



print(word_count(book_text))
print(count_letters(book_text))
print(sentance_counter(book_text))
print(ari(book_text))
