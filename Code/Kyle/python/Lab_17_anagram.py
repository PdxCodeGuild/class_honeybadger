#Anagram


welcome = print("Welcome to Anagram Checker")

first_word = input("First Word:").lower()
second_word = input("Second Word:").lower()
# printing variable values


first_word = first_word.replace(" ","")
second_word = second_word.replace(" ","")

first_word = list(first_word)
second_word = list(second_word)

first_word.sort()
second_word.sort()

print(first_word)

print(second_word)
if first_word == second_word:
  print("Words are anagrams")
else:
    print("Words are not anagrams")
