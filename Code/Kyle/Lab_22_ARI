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




# ari_scale = {
#      1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
#      2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
#      3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
#      4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
#      5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
#      6: {'ages': '10-11', 'grade_level':    '5th Grade'},
#      7: {'ages': '11-12', 'grade_level':    '6th Grade'},
#      8: {'ages': '12-13', 'grade_level':    '7th Grade'},
#      9: {'ages': '13-14', 'grade_level':    '8th Grade'},
#     10: {'ages': '14-15', 'grade_level':    '9th Grade'},
#     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
#     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
#     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
#     14: {'ages': '18-22', 'grade_level':      'College'}

