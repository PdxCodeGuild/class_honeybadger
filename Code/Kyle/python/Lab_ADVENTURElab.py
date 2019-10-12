import random

def anagram_check():
    print("Our traveler encounters a bandit! Complete the challenge or your story ends here! ")
    print("Type two words that, when put in alphabetical order, are the same")
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
      print('Our journey continues')
    else:
        print("The traveler failed the challenge and was executed.")
        exit()


def no_battle():
    print("No enemies were in sight, the traveler continues")



def word_challenge_hillside():
    user_input = input("enter a word that is the same word spelled backwards! ")
    if user_input == user_input[::-1]:
        print("You almost slipped! but caught your self and made it safely down the mountain.")
    else:
        print("You lost your grip and a loose rock gave way, you fell to your death.")
        exit()

def word_challenge_regular():
    user_input = input("enter a word that is the same word spelled backwards! ")
    if user_input == user_input[::-1]:
        print("Good job! Not dead yet!")
    else:
        print("You failed the challenge and got executed by the Bandit.")
        exit()

def battle_sequence():
    print("OUR TRAVELER HAS ENCOUNTERED AN ENEMY")
    choices = ["sword", "arrows", "magic"]
    # tie_outcomes = ["sword vs sword",  "punch vs punch", "arrows vs arrows"]
    user_wins = ["taco vs magic", "taco vs sword", "taco vs arrows", "arrows vs sword", "magic vs arrows", "sword vs magic"]
    cpu_win = ["sword vs magic", "arrows vs sword", "magic vs arrows"]

    user_choice = input("CHOOSE YOUR ATTACK: Sword, Arrows, or Magic? ").lower()
    if user_choice not in choices:
        print("Enter a valid attack")
    cpu_choice = random.choice(choices)
    outcome = user_choice + " vs " + cpu_choice

    if outcome in user_wins:
        print("THE TRAVELER HAS OVERCOME THE ENEMY")
    else:
        print("Our traveler was slayn by the enemy. The story ends here.")
        exit()









story_options = [no_battle, battle_sequence, anagram_check]
name = input("Hello traveler, What is your name? ")
user_input = input(f'{name} your mission is to travel through the forest and find the hidden jewls. As you travel through the forest, you approach a cave, and a path around the cave which do you choose? (cave/path) ').lower()

if user_input == "cave":
    random.choice(story_options)()
    user_input = input("As you reach the end of the cave, it opens up back into the forest. As light is fading you wonder if you should rest, or continue on. (rest/continue) ")
    if user_input == "rest":
        print("The traveler slept, and was killed by bandits.")
        exit()
    elif user_input == "continue":
        print("the traveler continues into the forest.")
elif user_input == "path":
    print("The traveler travels around the cave and continues into the forest.")

hillside_input = input(f'{name}, you seemingly reach the end of the forest, a sunken shipyard is seen in the distance. You know the jewls will be hidden there. 2 paths can take you there, down the hill side, or continue on the path you are on. (hillside/path)')
if user_input == "hillside":
    print("The hillside is a dangerous way to travel! complete the challenge or your story ends here!")
    word_challenge()
else:
    random.choice(story_options)()

shipyard_input = input(f'{name}, you are in the shipyard, a dense fog is covering almost everything in sight, but you notice a chest at the end of one of the docks. Alternativly, you can continue forwards. (continue/chest')

if shipyard_input == "chest":
    fight_or_run = input("You open the chest and you find that it was a trap! you can either run, or stay and fight the bandits! (fight/run)")
    if fight_or_run == "fight":
        print("You've chosen to stay and fight! ")
        battle_sequence()
        print("As you are walking over the body of your attacker, you notice.. THE JEWLS! He was carrying them in a small purse! You sweep them up and begin to run from the shipyard, as you turn the corner the King Bandit is there! You mustthe challenges and defeat him in order to escape!")
        anagram_check()
        word_challenge()
        battle_sequence()

    else:
        print("In your effort to flee you were shot by arrows and drowned. You were eaten by a shark. Dont be a woose.")

print(f'{name}, you won! Good job loser')
