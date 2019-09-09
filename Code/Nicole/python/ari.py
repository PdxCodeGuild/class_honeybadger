# ari.py

import re
import requests

def ari(text):
    pattern_words = "[a-zA-Z-]+"
    pattern_chars = "[a-zA-Z]"
    pattern_sent = "[\.\?\!]."

    words = len(re.findall(pattern_words, text))
    chars = len(re.findall(pattern_chars, text))
    sent = len(re.findall(pattern_sent, text))

    ari_compute = round((4.71 * (chars / words)) + (0.5 * (words / sent)) - 21.43)
    if ari_compute > 14:
        ari_compute = 14
    return ari_compute

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

book_name = "The Bible"
my_book = requests.get("https://www.gutenberg.org/cache/epub/10/pg10.txt")
book_text = my_book.text

num = ari(book_text)

print(f"\nThe ARI for {book_name} is {num}.\nThis corresponds to the {ari_scale[num]['grade_level']} level of difficulty\nwhich is suitable for an average person {ari_scale[num]['ages']} years old.")

