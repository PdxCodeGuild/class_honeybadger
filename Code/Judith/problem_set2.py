#filename: problem_set2.py

import random
import string

#problem 1
"""phrase = input('phrase')
splitphrase = list(phrase)
dubphrase = ''
for i in range(len(splitphrase)):
    dubphrase += 2*splitphrase[i]
print(dubphrase)"""

#problem 2
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
"""phrase = input('phrase...')
count = 0
while 'hi' in phrase:
    count +=1
    phrase = phrase.replace('hi','',1)    
print(count)"""

#problem 5
"""phr = input('phrase...')
def chk(phr):
    if phr.count('cat') == phr.count('dog'):
        return True
    else:
        return False
print(chk(phr))"""

#problem 6
"""phr = input('phrase...')
letter = input('letter')
print(phr.count(letter))"""

#problem 7
"""phr = input('phrase...')
phr = phr.replace(' ','') 
phr = phr.lower() 
print(phr)"""



        



