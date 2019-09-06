

import codecs

user_input = input("Please enter a message you would like to encode ")
def rot13encoding():
  print(codecs.encode(user_input, "rot_13"))

rot13encoding()