# lab_26_adventure.py

import random
import ascii_art

def challenge(health, money, distance):
    health_loss = [
        "You tripped on an electric scooter. ",
        "health_loss 2",
        "health_loss 3"
        ]
    health_gain = [
        "health_gain 1",
        "health_gain 2",
        "You grabbed a coffee at Stumptown. "
        ]
    money_loss = [
        "money_loss 1",
        "money_loss 2",
        "money_loss 3",
        ]
    money_gain = [
        "money_gain 1",
        "money_gain 2",
        "money_gain 3",
        ]
    distance_loss = [
        "distance_loss 1",
        "distance_loss 2",
        "distance_loss 3",
        ]
    distance_gain = [
        "distance_gain 1",
        "distance_gain 2",
        "distance_gain 3",
        ]
    play = random.choice([health_loss, health_gain, money_loss, money_gain, distance_loss, distance_gain])
    num = random.randint(0, len(play)-1)
    game_choice_play = play[num]
    print(game_choice_play)
    return play

def adventure(player, health = 100, money = 100, distance = 100):
    # while True:
    for i in range(11):
        status = f"\nStatus:\n\tHealth = {health}\n\tMoney = ${money} \n\t{distance} miles to destination\n"
        print(status)
        play = challenge(health, money, distance)
        print(play)
    
        play_amount = random.randint(1,10)
        if health_loss in play:
            health -= play_amount
            print(f"Your health decreased {play_amount}")
        elif health_gain in play:
            health += play_amount
            print(f"Your health increased {play_amount}")
        # elif play in money_loss:
        #     money -= play_amount
        #     print(f"Your money decreased ${play_amount}")
        # elif play in money_gain:
        #     money += play_amount
        #     print(f"Your money increased ${play_amount}")
        # elif play in distance_loss:
        #     distance -= play_amount
        #     print(f"Your distance decreased {play_amount} miles")
        # elif play in distance_gain:
        #     distance += play_amount
        #     print(f"Your distance increased {play_amount} miles")



print("\nWelcome to \"The Portland Trail\"! Let's see if you can navigate your way through Portland.\n")
player_name = input("What is your name? ")
adventure(player_name)