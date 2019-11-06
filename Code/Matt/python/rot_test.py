
def rot13(phrase):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out_phrase = ""
   for char in phrase:
       out_phrase += abc[(abc.find(char)+13)%26]
   return out_phrase

print(rot13("cat"))
