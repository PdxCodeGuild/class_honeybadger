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
    for i in range(len(contents)):
        print(contents[i])
    print(contents)
    # book_contents = book_contents.split(" ")
    return contents

result = count_words("book_test.txt")

# print(result)

exit()

def word_count(contents):
    contents = list(contents)
    print(contents)
    book_dict = {}
    for i in range(len(contents)):
        for j in book_dict:
            if contents[i] != book_dict[j]:
                book_dict.update(contents[i], 1)

    return book_dict


print(word_count(result))
