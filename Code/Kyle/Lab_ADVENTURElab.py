import random




def no_battle():
    print("No enemies were in sight, the traveler continues")







def battle_sequence():
    print("OUR TRAVELER HAS ENCOUNTERED AN ENEMY")
    choices = ["sword", "arrows"]
    # tie_outcomes = ["sword vs sword",  "punch vs punch", "arrows vs arrows"]
    user_wins = ["m vs sword", "m vs arrows", "arrows vs sword", "sword vs punch", "punch vs arrows"]
    cpu_win = ["sword vs arrows", "punch vs sword", "arrows vs punch"]

    user_choice = input("CHOOSE YOUR ATTACK: Sword, or Arrows? ").lower()
    cpu_choice = random.choice(choices)
    outcome = user_choice + " vs " + cpu_choice

    if outcome in user_wins:
        print("THE TRAVELER HAS OVERCOME THE ENEMY")
    elif outcome in cpu_win:
        print("Our traveler was slayn by the enemy. The story ends here.")
    else:
        print("Please enter a valid attack.")








story_options = [no_battle, battle_sequence]

user_input = input("The traveler approaches a cave, and a path around the cave. Which does the traveler choose? (cave/path) ")

if user_input == "cave":
    random.choice(story_options)()
    user_input = input("As the traveler reaches the end of the cave, it opens up back into the forest. As light is fading the traveler wonders if he should rest, or continue. (rest/continue) ")
    if user_input == "rest":
        print("The traveler slept, and was killed by bandits.")
        exit()
    elif user_input == "continue":
        print("the traveler continues into the forest.")
elif user_input == "path":
    print("The traveler continues around the cave and continues into the forest.")
