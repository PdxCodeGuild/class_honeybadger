'''
Palindrome

A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal 
to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome

Anagram

Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, 
False if they're not. The procedure for comparing the two strings is as follows:

    Convert each word to lower case (lower)
    Remove all the spaces from each word (replace)
    Sort the letters of each word (sorted)
    Check if the two are equal

>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams

'''
#Using a loop to iterate thru each element of the word
def check_palindrome(word):
    str = '' #---> creating an empty string variable that will collect each letter in word

    #loops thru each element in word, adds the element to the variable str.  
    #str continues to build and adds each new element to the beginning or before the latest elment.
    #end result appears to be a reversed list of the original word
    for i in word: 
        str = i + str
        #print(str)
    print(f'You entered the word {word} and its reverse is {str}')
    print()

    if str == word:
        print(f'The word {word.upper()} is a palindrome.')
    else:
        print(f'The word {word} is not a palindrome.')
        
    return word

user_input = input('Please enter a word ')
#print(user_input)
print()

check_palindrome(user_input)

def check_anagram(word1, word2):
    word1 = word1.lower() #---> converting word to lowercase
    word1 = word1.replace(' ', '') #---> removing the blank spaces by replacing with no blank spaces 
    #print(sorted(word1)) #---> can use print/sorted to returns new sorted list. sorted returns list, sort returns nothing
    word1sorted = sorted(word1) #---> sorting word1 and storing in new variable, returns sorted word in a list
    
    word2 = word2.lower() #---> converting word to lowercase
    word2 = word2.replace(' ', '') #---> removing the blank spaces by replacing with no blank spaces 
    #print(sorted(word2)) #---> can use print/sorted to returns new sorted list. sorted returns list, sort returns nothing
    word2sorted = sorted(word2) #---> sorting word2 and storing in new variable, returns sorted word in a list
    
    if word1sorted == word2sorted:
        print(f'The words {word1.upper()} and {word2.upper()} are equal and can be rearranged to fit each other. They are Anagrams!')
    else:
        print(f'The words {word1.upper()} and {word2.upper()} are not the same, thus are not Anagrams')


    print(f'word1 = {word1}, word2 = {word2}, word1 sorted = {word1sorted}, word2 sorted = {word2sorted}')

    #return word1, word2
    
firstword = input('Enter 1st word ')
secondword = input('Enter 2nd word ')
check_anagram(firstword, secondword)




