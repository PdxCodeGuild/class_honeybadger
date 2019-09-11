# pig_latin.py


# convert string to list
# if beginning starts with vowel:
# -- print "yay" after word
# if word normal word:
# -- move first letter to end, add "yay"

# thing = [t[0] for t in list_thing if t[1] == list_thing[0][1]]

def pig_latin(phrase):
    phrase = phrase.split()
    phrase_2 = phrase.split()
    
    new_phrase = []
    pig_phrase = []
    vowel = ["a", "e", "i", "o", "u", "w", "y"]
    for i in range(len(phrase)):
        new_phrase.append([phrase[i]]) # creates list of list with words from the phrase
        
        # for q in range(len(new_phrase)):
        #     print(new_phrase[q])
        #     new_phrase[i].append(new_phrase[q])
        #     print(new_phrase)

    #     for x in range(len(new_phrase)):
    #         for y in range(len(new_phrase[x])):
    #             if new_phrase[x][y][0] not in vowel:
    #                 new_phrase.insert(new_phrase[x][y][-1], new_phrase[x][y][0])
    #                 new_phrase.remove(new_phrase[x][y][0])
    #                 new_phrase.insert(new_phrase[x][y][-1], "yay")
    # 
    # print(new_phrase)
    # print(pig_phrase)
    # return pig_phrase


user_input = input("Please type a phrase: ").lower()
print(pig_latin(user_input))

# my_list = [["this", "that", "other"], ["one", "two", "three"], ["my", "happy", "place"]]
# 
# print(my_list[0])
# print(my_list[0][0][0])