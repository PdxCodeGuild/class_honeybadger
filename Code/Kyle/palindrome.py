def reverse(word1):
  if(len(word1) == 0):
    return word1
  else:
    return reverse(word1[1 : ]) + word1[0]


word = raw_input('Enter a word: ')
word1 = reverse(word)
print("Reversed:  ", word1)

if(word == word1):
  print("word is a palindrome")
else:
  print("no word is not a palindrome")
