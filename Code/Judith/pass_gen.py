#filename: pass_gen.py

 #mods
import random
import string

 #define variables
lettnum=int(input("How many letters do there need to be? "))
numnum=int(input("How many digits do you need? "))
puncnum=int(input("How many items of punctuation do you need? "))
password=""

#generate characters
for x in range(int(lettnum)):
    password+=(random.choice(string.ascii_letters))
for x in range(int(numnum)):
    password+=(random.choice(string.digits))
for x in range(int(puncnum)):
    password+=(random.choice(string.punctuation))

#randomize placement
password=list(password)

random.shuffle(password)

password=''.join(password)

#final result
print(password)
