#filename: lab22_arigen.py

import string
import re
import math

import string

with open('ulysses.txt', 'r') as f:
    contents = f.read()

charcount = len(re.findall(r'[\S]',contents))
wordcount = len(re.findall(r'[\w]+',contents))
sencount = len(re.findall(r'[.]',contents))

print(charcount)
print(wordcount)
print(sencount)

def arigen(charcount,wordcount,sencount):
    scorebase = 4.71*(charcount/wordcount) + 0.5*(wordcount/sencount) - 21.43
    scorebase = math.ceil(scorebase)
    if scorebase > 14:
        scorebase = 14
    return scorebase
print(arigen(charcount,wordcount,sencount))
