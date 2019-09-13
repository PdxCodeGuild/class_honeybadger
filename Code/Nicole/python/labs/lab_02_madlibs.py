# lab_02_madlibs.py

import random

# version 1:

# def madlibs():
#     adjective_1 = input("Please enter an adjective: ").upper()
#     noun_1 = input("Please enter a noun: ").upper()
#     verb_1 = input("Please enter a verb (past tense): ").upper()
#     adverb_1 = input("Please enter an adverb: ").upper()
#     adjective_2 = input("Please enter an adjective: ").upper()
#     noun_2 = input("Please enter a noun: ").upper()
#     noun_3 = input("Please enter a noun: ").upper()
#     adjective_3 = input("Please enter an adjective: ").upper()
#     verb_2 = input("Please enter a verb: ").upper()
#     adverb_2 = input("Please enter an adverb: ").upper()
#     verb_3 = input("Please enter a verb (past tense): ").upper()
#     adjective_4 = input("Please enter an adjective: ").upper()
# 
#     return print(f"Today I went to the zoo. I saw a {adjective_1} {noun_1} jumping up and down in its tree. He {verb_1} {adverb_1} through the large tunnel that led to its {adjective_2} {noun_2}. I got some peanuts and passed them through the cage to a gigantic gray {noun_3} towering above my head. Feeding that animal made me hungry. I went to get a {adjective_3} scoop of ice cream. It filled my stomach. Afterwards I had to {verb_2} {adverb_2} to catch our bus. When I got home I {verb_3} my mom for a {adjective_4} day at the zoo.")

# version 2:

# def madlibs():
#     adjective = input("Please enter FOUR adjectives, separated by spaces: ").upper().split(" ")
# 
#     x = random.choice
# 
#     noun = input("Please enter THREE nouns, separated by spaces: ").upper().split(" ")
# 
#     verb_pt = input("Please enter TWO past-tense verbs, separated by spaces: ").upper().split(" ")
# 
#     verb = input("Please enter ONE regular verb: ").upper().split(" ")
# 
#     adverb = input("Please enter TWO adverbs, separated by spaces: ").upper().split(" ")
# 
#     print(f"Today I went to the zoo. I saw a {x(adjective)} {x(noun)} jumping up and down in its tree. He {x(verb_pt)} {x(adverb)} through the large tunnel that led to its {x(adjective)} {x(noun)}. I got some peanuts and passed them through the cage to a gigantic gray {x(noun)} towering above my head. Feeding that animal made me hungry. I went to get a {x(adjective)} scoop of ice cream. It filled my stomach. Afterwards I had to {x(verb)} {x(adverb)} to catch our bus. When I got home I {x(verb_pt)} my mom for a {x(adjective)} day at the zoo.\n")
# 
#     print("Thanks for playing!")


# version 3:

def madlibs():
    play_again = "yes"
    while play_again == "yes":
        adjective = input("Please enter FOUR adjectives, separated by spaces: ").upper().split(" ")

        x = random.choice

        noun = input("Please enter THREE nouns, separated by spaces: ").upper().split(" ")

        verb_pt = input("Please enter TWO past-tense verbs, separated by spaces: ").upper().split(" ")

        verb = input("Please enter ONE regular verb: ").upper().split(" ")

        adverb = input("Please enter TWO adverbs, separated by spaces: ").upper().split(" ")

        repeat = "yes"
        while repeat == "yes":
            print(f"Today I went to the zoo. I saw a {x(adjective)} {x(noun)} jumping up and down in its tree. He {x(verb_pt)} {x(adverb)} through the large tunnel that led to its {x(adjective)} {x(noun)}. I got some peanuts and passed them through the cage to a gigantic gray {x(noun)} towering above my head. Feeding that animal made me hungry. I went to get a {x(adjective)} scoop of ice cream. It filled my stomach. Afterwards I had to {x(verb)} {x(adverb)} to catch our bus. When I got home I {x(verb_pt)} my mom for a {x(adjective)} day at the zoo.")
            repeat = input("Would you like to hear the story again? Please type 'yes' or 'no': ")

        play_again = input("Would you like to play again? Please type 'yes' or 'no': ")


madlibs()
