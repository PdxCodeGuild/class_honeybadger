# count_words.py

import string

def count_words(book):
    punct = str.maketrans("", "", string.punctuation)
    with open(book, "r") as our_book:
        contents = our_book.read().lower()
    contents = contents.replace("\n", "")
    contents = contents.translate(punct)
    contents = contents.split(" ")
    return contents

result = count_words("book_test.txt")
# print(result)

def word_count(contents):
    book_dict = {}
    for word in contents:

    return book_dict


print(word_count(result))
