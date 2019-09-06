

def anagram_checker(word1, word2):
    if(sorted(word1) == sorted(word2)):
        print("These words are anagrams.")
    else:
        print("Not anagrams.")

        ### Note to Justin ###

        #the problem i was having earlier was resolved by using "raw_input" instead of input. I'm not sure if this is something you want us doing but it allowed my code to run on atom...


user_input = raw_input("Enter a word... ")
user_input2 = raw_input("Enter another word... ")
word1 = user_input.replace(" ", "" )
word2 = user_input2.replace(" ", "")


anagram_checker(word1, word2)
