#filename: problem_set2.py

import random
import string

#problem 1
# Get a string from the user, print out another string, doubling every letter.
"""phrase = input('phrase')
splitphrase = list(phrase)
dubphrase = ''
for i in range(len(splitphrase)):
    dubphrase += 2*splitphrase[i]
print(dubphrase)"""

#problem 2
# Write a function that takes a string, and returns a list of strings, each missing a different character.
"""phrase = input()
def remr(phrase):
    splitphrase = list(phrase)
    splitphrase.pop(random.randint(0,len(splitphrase)-1))
    #print(splitphrase)
    modphrase = ''.join(splitphrase)
    return modphrase
for i in range(len(phrase)):
    print(remr(phrase))"""

#problem 3
# Return the letter that appears the latest in the english alphabet.
"""letters = string.ascii_lowercase
phrase = input('phrase...')
def findlast(phrase,letters):
    lis = list(phrase)
    hi = 0
    for i in range(len(lis)):
        cur = letters.find(lis[i])
        if cur > hi:
            hi = cur
    return hi
print(letters[findlast(phrase,letters)])"""

#problem 4
# Write a function that returns the number of occurances of 'hi' in a given string.
"""phrase = input('phrase...')
count = 0
while 'hi' in phrase:
    count +=1
    phrase = phrase.replace('hi','',1)    
print(count)"""

#problem 5
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
"""phr = input('phrase...')
def chk(phr):
    if phr.count('cat') == phr.count('dog'):
        return True
    else:
        return False
print(chk(phr))"""

#problem 6
# Return the number of letter occurances in a string.
"""phr = input('phrase...')
letter = input('letter')
print(phr.count(letter))"""

#problem 7
# Convert input strings to lowercase without any surrounding whitespace.
"""phr = input('phrase...')
phr = phr.replace(' ','') 
phr = phr.lower() 
print(phr)"""



        



