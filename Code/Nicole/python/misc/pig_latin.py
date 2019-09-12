# pig_latin.py


# convert string to list
# if beginning starts with vowel:
# -- print "yay" after word
# if word normal word:
# -- move first letter to end, add "yay"

# thing = [t[0] for t in list_thing if t[1] == list_thing[0][1]]

def pig_latin(phrase):
    phrase = phrase.split()
    
    
    # phrase[list][word][letter]
              # x   
    
    new_phrase = []
    pig_phrase = []
    
    vowel = ["a", "e", "i", "o", "u", "y"]
    punct = [".", ",", "'", "!", "?"]
    th = ["th"]
    
    for x in range(len(phrase)):
        new_phrase.append([phrase[x]]) # creates list of list with words from the phrase
    for y in range(len(new_phrase)): 
        #iterating through the sub-lists (words) in the list:
        if new_phrase[y][0][-1] in punct: 
            # this handles the punctuation properly
            if new_phrase[y][0][0] in vowel:
                pig_phrase.append(new_phrase[y][0][:-1] + "yay" + new_phrase[y][0][-1])
            elif new_phrase[y][0][0] == "t" and new_phrase[y][0][1] == "h":
                    pig_phrase.append(new_phrase[y][0][2:-1] + new_phrase[y][0][0:2] + "ay" + new_phrase[y][0][-1])
            else:
                # print(new_phrase[y][0][1:-1])
                pig_phrase.append(new_phrase[y][0][1:-1] + new_phrase[y][0][0] + "ay" + new_phrase[y][0][-1])
        # if no punctuation, this part goes:
        elif new_phrase[y][0][0] in vowel:
            pig_phrase.append(new_phrase[y][0][0:] + "yay")
        # this handles words that start with "th"
        elif new_phrase[y][0][0] == "t" and new_phrase[y][0][1] == "h":
                pig_phrase.append(new_phrase[y][0][2:] + new_phrase[y][0][0:2] + "ay")
        else:
            pig_phrase.append(new_phrase[y][0][1:] + new_phrase[y][0][0] + "ay")
    
    pig_phrase_2 = " ".join(pig_phrase).capitalize()
    return pig_phrase_2


user_input = input("Please type a phrase: ").lower()
print(pig_latin(user_input))

# my_list = [["this"], ["one"], ["my"]]
# 
# 
# print(my_list)
# print(my_list[0][0][0]) # first letter of first item in first list
# print(my_list[0][0][1:] + my_list[0][0][0] + "ay") # consanent
# print(my_list[1][0][0:] + "yay") # starts with a vowel
# print(my_list[2][0][1:] + my_list[2][0][0] + "ay") # consanent