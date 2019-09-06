

def anagram_checker(word1, word2):
    count1 = 0
    count2 = 0

    for i in word1:
        count1[ord(i)] += 1
    for i in word2:
        count2[ord(i)] += 1
    if len(word1) != len(word2):
        print("not anagrams")
    else:
        print("anagrams")


word1 = input("Enter first word").lower()
word2 = input("Enter second word").lower()
if(anagram_checker(word1, word2)):
    print("the two strings are anagram")
else:
    print("the two strings are not anagrams")
