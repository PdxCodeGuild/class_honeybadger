# lab_26_adventure_classes.py

import random

class Adventure:
    def __init__(self, player, health = 100, money = 100, distance = 100):
        self.player = player
        self.health = health
        self.money = money
        self.distance = distance
    
    def challenge(self):
        self.health = 100
        self.money = 100
        self.distance = 100
        for i in range(11):
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
            
            play_amount = random.randint(1,10)
            if play in list(health_loss):
                self.health -= play_amount
                print(f"Your health decreased {play_amount}")
            elif play in list(health_gain):
                self.health += play_amount
                print(f"Your health increased {play_amount}")
            elif play in list(money_loss):
                self.money -= play_amount
                print(f"Your money decreased ${play_amount}")
            elif play in list(money_gain):
                self.money += play_amount
                print(f"Your money increased ${play_amount}")
            elif play in list(distance_loss):
                self.distance -= play_amount
                print(f"Your distance decreased {play_amount} miles")
            elif play in list(distance_gain):
                self.distance += play_amount
                print(f"Your distance increased {play_amount} miles")
    
            status = f"\nStatus:\n\tHealth = {self.health}\n\tMoney = ${self.money} \n\t{self.distance} miles to destination\n"
            print(status)
            

print("\nWelcome to \"The Portland Trail\"! Let's see if you can navigate your way through Portland.\n")
player_name = input("What is your name? ")
p = Adventure(player_name)
p.challenge()