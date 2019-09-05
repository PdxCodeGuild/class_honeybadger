# test.py

def missing_char(word):
    word_list = []
    for char in range(len(word)):
        word_list.append(word[:char] + word[char + 1:])
    return word_list
    
print(missing_char("pizza"))