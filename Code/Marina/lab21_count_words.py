
import string

# load file​
with open('ThroughtheDesert.txt', 'r') as f:
    contents = f.read()
#print(contents)

# turn all chars to lower case ans split​
def string_modifier(contents):
    results = ''
    contents = contents.lower()
    for char in contents:
        if char not in string.punctuation:
            results += char
    results = results.split()
    return results
result = string_modifier(contents)
#print(string_modifier(contents))


# create a dict​ with unique words as keys
def dicreator(result):
    wdic = {}
    for word in result:
        if word not in wdic:
            wdic[word] = 0
        wdic[word] +=1
    return wdic
# sets variable wdic as the dict
wdic = dicreator(result)


# identify and print the top ten most used words​
def topten(wdic):
    words = list(wdic.items())
    words.sort(key=lambda tup:tup[1], reverse=True)
    for i in range(min(10,len(words))):
        print(words[i])
topten(wdic)
