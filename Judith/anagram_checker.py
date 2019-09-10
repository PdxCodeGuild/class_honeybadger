#filename: anagram_checker.py

#Welcome statement
print("We will be asking you to print two strings of characters, and we will tell you if they represent an anagram")

#user inputs
phrase_one=input("Please type something\n")
phrase_two=input("Now type something else\n")

#convert strings to lists
phrase_one=phrase_one.lower()
phrase_two=phrase_two.lower()

phrase_one=phrase_one.replace(" ","")
phrase_two=phrase_two.replace(" ","")

phrase_one=list(phrase_one)
phrase_two=list(phrase_two)

list.sort(phrase_one)
list.sort(phrase_two)

print(phrase_one,"\n",phrase_two)

#comparison
if phrase_one==phrase_two:
    print("This is an anagram")
else:
    print("This is not an anagram")
