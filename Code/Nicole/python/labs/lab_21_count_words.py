# lab_21_count_words.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab21-count_words.md

import re
import string

def count_words(book):
    with open(book, "r") as our_book:
        contents = our_book.read().lower()
    # pattern = "(?![\._]\.){P}"
    contents = list(contents)
    punct = list(string.punctuation)
    punct += "”"
    new_contents = []
    for i in range(len(contents)):
        if contents[i] not in punct:
            new_contents.append(contents[i])
        else:
            new_contents.append(" ")
    new_contents = list("".join(new_contents).split())
    
    contents_no_dupes = {}
    for j in range(len(new_contents)):
        if new_contents[j] not in contents_no_dupes:
            contents_no_dupes[new_contents[j]] = 1
        else:
            contents_no_dupes[new_contents[j]] += 1
    
    top_ten = []
    words = list(contents_no_dupes.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(len(words)):
        top_ten.append(words[i])
    
    top_ten = top_ten[:10]
    
    
    
    return top_ten

result = count_words("dancers_dark_book.txt")

print(f"Top ten = {result}")

exit()
