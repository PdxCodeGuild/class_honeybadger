#Filename: lab21_wordcount.py

import string
import re

with open('ThroughtheDesert.txt', 'r') as f:
    contents = f.read()

# print(contents)

def string_modifier(contents):
    results = ''
    contents = contents.lower()
    for char in contents:
        if char not in string.punctuation:
            results += char
    results = results.split()
    return results

result = string_modifier(contents)
# print(result)

def dicreator(result):
    wdic = {}
    for word in result:
        if word not in wdic:
            wdic[word] = 0
        wdic[word] += 1
    return wdic

wdic = dicreator(result)
# print(wdic)

def topten(wdic):
    words = list(wdic.items())
    words.sort(key=lambda tup:tup[1], reverse=True)
    for i in range(min(10,len(words))):
        print(words[i])

# topten(wdic)

def pair_finder(result):
    pair_data = {}
    for i in range(len(result)-1):
        pair = (result[i], result[i+1])
        if pair not in pair_data:
            pair_data[pair] = 0
        pair_data[pair] += 1

    pair_data = list(pair_data.items())
    pair_data.sort(key=lambda tup:tup[1], reverse=True)
    for i in range(min(10,len(pair_data))):
        print(pair_data[i])
    



# print(pair_finder(result))




    








            

