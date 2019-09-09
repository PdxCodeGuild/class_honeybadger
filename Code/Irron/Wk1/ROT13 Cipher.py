#create dictionary
dictionary = {
    "a" : "n",
    "b" : "o",
    "c" : "p",
    "d" : "q",
    "e" : "r",
    "f" : "s",
    "g" : "t",
    "h" : "u",
    "i" : "v",
    "j" : "w",
    "k" : "x",
    "l" : "y",
    "m" : "z",
    "n" : "a",
    "m" : "b",
    "o" : "c",
    "p" : "d",
    "q" : "e",
    "r" : "f",
    "s" : "g",
    "t" : "h",
    "u" : "i",
    "v" : "j",
    "w" : "k",
    "x" : "l",
    "y" : "m",
    "z" : "n",
}

# print(cipher)
#
# test = cipher["r"] 
# print(test)

user_input_1 = input("Please enter 1st letter ")
#user_input_2 = input("Please enter 2nd letter")

# answer = cipher[user_input_1]
# print(answer)

#user_input_seperate = user_input.split(sep= "")
#print(user_input_seperate)


#iterate user input
for char in user_input_1:
    print(char)
#iterate dictionary

for key in dictionary:
    value = dictionary[key]
    print(key)


def rotn(text, n):
    alphabet 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n

    while index >= len(alphabet):#while index is beyond alphabet
        index -= len(alphabet)

   #if index >= len(alphabet):
    #   index -= len(alphabet)
    output += alphabet[index]   
    
    return output
print(rotn('justin', 13))