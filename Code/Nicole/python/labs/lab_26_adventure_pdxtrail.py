# lab_26_adventure_pdxtrail.py

import random
import ascii_art
import time

# this slows down the printing of the text
def print_sleep(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(.025)

# this slows down the printing of the text, but makes it go a little faster
def print_fast(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(.01)

def print_ascii(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(.001)


# Main game, starts out with default settings for health/money/etc
class Adventure:
    def __init__(self, player, health = 30, money = 50, distance = 10, time = 25, sleep = 2):
        self.player = player
        self.health = health
        self.money = money
        self.distance = distance
        self.time = time
        self.sleep = sleep
        
        
    
    def health(self):
        if_play = random.choice([True, False])
        if if_play:
            neg_num = random.randint(-10, -1)
            pos_num = random.randint(1, 10)
            events = [
                {"text" : "You got attacked by a honeybadger", "health" : neg_num, "ascii" : ascii_art.badger},
                {"text" : "You slipped in some moss on the street and broke your pinky toe", "health" : neg_num, "ascii" : ascii_art.foot},
                {"text" : "The Gorge caught fire again and you forgot your emergency respirator", "health" : neg_num, "ascii" : ascii_art.fire},
                # {"text" : "xxxxxxx", "health" : neg_num},
                # {"text" : "xxxxxxx", "health" : neg_num},
                # {"text" : "xxxxxxx", "health" : neg_num},
                # {"text" : "xxxxxxx", "health" : neg_num},
                # {"text" : "xxxxxxx", "health" : neg_num},
                {"text" : "They had free coffee samples at Stumptown", "health" : pos_num, "ascii" : ascii_art.coffee},
                # {"text" : "xxxxxxx", "health" : pos_num},
                # {"text" : "xxxxxxx", "health" : pos_num}
                ]
            choose_event = random.choice(events)
            if choose_event["health"] < 0:
                plus_minus = "decreased"
            else:
                plus_minus = "increased"
            print_ascii(f"\n{choose_event['ascii']}\n")
            print_sleep(f"\n{choose_event['text']}.\n  --> Your HEALTH is {plus_minus} by {abs(choose_event['health'])}.\n\n")
            self.health += choose_event["health"]
            time.sleep(self.sleep)
        return if_play
    
    def money(self):
        if_play = random.choice([True, False])
        if if_play:
            neg_num = random.randint(-10, -1)
            pos_num = random.randint(1, 10)
            events = [
                {"text" : "You got distracted and stocked up at a nearby dispensary", "money" : neg_num + neg_num, "ascii" : ascii_art.mj},
                {"text" : "You handed over some cash to a homeless person", "money" : neg_num, "ascii" : ascii_art.person_sleeping},
                {"text" : "You found an old parking ticket in your car you forgot to pay", "money" : neg_num, "ascii" : ascii_art.police},
                {"text" : "You got guilted into donating to a political cause from a person standing on a corner", "money" : neg_num, "ascii" : ascii_art.person_sign},
                {"text" : "Your gas light just came on and you have to stop to fill up the tank", "money" : neg_num, "ascii" : ascii_art.car_2},
                # {"text" : "xxxxxxx", "money" : neg_num, "ascii" : ascii_art.car},
                # {"text" : "xxxxxxx", "money" : neg_num, "ascii" : ascii_art.car},
                # {"text" : "xxxxxxx", "money" : pos_num, "ascii" : ascii_art.car},
                # {"text" : "xxxxxxx", "money" : pos_num, "ascii" : ascii_art.car},
                {"text" : "A friend Venmo'd you some cash they owed you", "money" : pos_num, "ascii" : ascii_art.dollar}
                ]
            choose_event = random.choice(events)
            if choose_event["money"] < 0:
                plus_minus = "lose"
            else:
                plus_minus = "gain"
            print_ascii(f"\n{choose_event['ascii']}\n")
            print_sleep(f"\n{choose_event['text']}.\n  --> You {plus_minus} ${abs(choose_event['money'])}.\n\n")
            self.money += choose_event["money"]    
            time.sleep(self.sleep)
        return if_play
    
    def distance(self):
        if_play = random.choice([True, False])
        if if_play:
            neg_num = random.randint(-2, 0)
            pos_num = random.randint(1, 3)
            events = [
                {"text" : "Your GPS failed you and you took a wrong turn", "distance" : pos_num, "ascii" : ascii_art.gps},
                {"text" : "There was an accident on the highway", "distance" : pos_num, "ascii" : ascii_art.police},
                {"text" : "You forgot that today is the naked bike race and had to take a detour", "distance" : pos_num, "ascii" : ascii_art.bike},
                {"text" : "You got stuck behind a bus and decided to go another way", "distance" : pos_num, "ascii" : ascii_art.bus},
                {"text" : "You had to evade a clown weilding an axe, which took you in the wrong direction", "distance" : pos_num, "ascii" : ascii_art.clown},
                {"text" : "An Instagrammer is taking selfies in the middle of the street and you have to take another route", "distance" : pos_num, "ascii" : ascii_art.camera},
                # {"text" : "xxxxxxx", "distance" : pos_num, "ascii" : ascii_art.car},
                # {"text" : "xxxxxxx", "distance" : pos_num, "ascii" : ascii_art.car},
                {"text" : "Good news! A new bridge was built and is a direct route to your destination", "distance" : neg_num, "ascii" : ascii_art.bridge},
                {"text" : "You jumped a ramp over a line of cars and got to the heaad of the pack", "distance" : neg_num, "ascii" : ascii_art.car},
                # {"text" : "xxxxxxx", "distance" : neg_num, "ascii" : ascii_art.car}
                ]
            choose_event = random.choice(events)
            if choose_event["distance"] < 0:
                plus_minus = f"decreased by {abs(choose_event['distance'])} miles."
            elif choose_event["distance"] == 0:
                plus_minus = "(amazingly) unchanged."
            else:
                plus_minus = f"increased by {abs(choose_event['distance'])} miles."
            print_ascii(f"\n{choose_event['ascii']}\n")
            print_sleep(f"\n{choose_event['text']}.\n  --> Your DISTANCE is {plus_minus}\n\n")
            self.distance += choose_event["distance"]
            time.sleep(self.sleep)
        return if_play
    
    def time(self):
        if_play = random.choice([True, False])
        if if_play:
            neg_num = random.randint(-2, 0)
            pos_num = random.randint(1, 3)
            events = [
                {"text" : "You're driving behind someone who refuses to go faster than five miles under the speed limit", "time" : neg_num, "ascii" : ascii_art.car},
                {"text" : "You discovered your clock was set wrong", "time" : pos_num, "ascii" : ascii_art.car},
                {"text" : "You saw a puppy and stopped your car to go pet it", "time" : neg_num, "ascii" : ascii_art.dog},
                {"text" : "It started to rain and everyone is driving slowly", "time" : neg_num, "ascii" : ascii_art.car},
                {"text" : "The bridge is up", "time" : neg_num, "ascii" : ascii_art.bridge},
                {"text" : "The Unipiper is in front of you and attracted a large crowd, slowing down traffic", "time" : neg_num, "ascii" : ascii_art.car_2}
                ]
            choose_event = random.choice(events)
            if choose_event["time"] < 0:
                plus_minus = f" lose {abs(choose_event['time'])} minutes."
            elif choose_event["time"] == 0:
                plus_minus = "r time is (amazingly) unchanged."
            else:
                plus_minus = f" get an extra {abs(choose_event['time'])} minutes."
            print_ascii(f"\n{choose_event['ascii']}\n")
            print_sleep(f"\n{choose_event['text']}.\n  --> You{plus_minus}\n\n")
            self.time += choose_event["time"]
            time.sleep(self.sleep)
        return if_play
    
    def death(self):
        death_event = random.randint(1, 100)
        death_event_2 = random.randint(1, 100)
        if death_event == death_event_2:
            print_ascii(f"\n\n\n{ascii_art.rip}")
            print_sleep("There was a massive earthquake and you fell into lava throuh a fissure in the pavement. You're now dead.\n")
            print_fast(f"\n\n{ascii_art.game_over}\n\n")
            exit()

    def problem(self):
        problem = random.choice(["health", "money", "time"])
        return problem
    
    def challenge(self, player):
        print_fast(f"\n\n* * * * * * * * * * * * * * * * * * * * * *\n* * * * * * * * * * * * * * * * * * * * * *\n\n{self.player}'s starting Status:\n\tHealth = {self.health}\n\tMoney = ${self.money} \n\t{self.time} minutes remaining\n\t{self.distance} miles to your destination\n\n* * * * * * * * * * * * * * * * * * * * * *\n* * * * * * * * * * * * * * * * * * * * * *\n\n")
        time.sleep(self.sleep)
        keep_playing = "yes"
        while self.health > 0 and self.money > 0 and self.time > 0:
            while keep_playing == "yes":
                self.time -= 2
                self.distance -= 1
                nothing = False
                Adventure.death(self)
                Adventure.time(self)
                Adventure.health(self)
                Adventure.money(self)
                Adventure.distance(self)
                # print("\n\nTest print:\n\n")
                # print_sleep(f"Health = {self.health}\n")
                # print_sleep(f"Money = {self.money}\n")
                # print_sleep(f"Time = {self.time}\n")
                # print_sleep(f"Distance = {self.distance}\n")
                status = f"\n\n* * * * * * * * * * * * * * *\n* * * * * * * * * * * * * * *\n\n{self.player}'s Status:\n\tHealth = {self.health}\n\tMoney = ${self.money} \n\t{self.time} minutes remaining\n\t{self.distance} miles to your destination\n\n* * * * * * * * * * * * * * *\n* * * * * * * * * * * * * * *\n\n"
                print_fast(status)

                # if all of the methods return false, then it returns a print statement (instead of a blank round)
                # if Adventure.time(self) is False and Adventure.health(self) is False and Adventure.money(self) is False and Adventure.distance(self) is False:
                #     print("\nYou made it through this round with nothing bad happening!")
                
                if self.time <= 0:
                    print_fast("You didn't get there in time.\n")
                    print_fast(f"\n\n{ascii_art.game_over}\n\n")
                    exit()
                elif self.health <= 0:
                    print_ascii(f"\n\n{ascii_art.rip}\n")
                    print("You died.")
                    print_fast(f"\n\n{ascii_art.game_over}\n\n")
                    exit()
                elif self.money <= 0:
                    print_fast(f"\n\n{ascii_art.game_over}\n\n")
                    print_fast("You ran out of money and can no longer afford to live in Portland.\n\n\n")
                    exit()
                elif self.distance <= 0:
                    print_ascii(ascii_art.beer)
                    print_fast("You made it to your destination! Time to celebrate.\n")
                    print_fast(f"\n\n{ascii_art.game_over}\n\n")
                    exit()
                # else:
                #     print_fast(status)
                keep_playing = input("Would you like to continue to your destination?\t").lower()
                if keep_playing == "no":
                    print_ascii(ascii_art.tent)
                    print_fast("\n\nYou gave up and moved into a tent on the side of the road.\n\n")
                    print_fast(f"\n\n{ascii_art.game_over}\n\n")
                    exit()
                    
                
            

player_name = input("\nWhat is your name? ")
print_fast(f"\nHello, {player_name}, and welcome to \"The Portland Trail\"!")
time.sleep(.5)
print_fast("\n\nLet's see if you can drive your way through Portland to your destination before you run out of money, time, or you die.\n")
time.sleep(1)
print_fast("\nEach round you will lose both time and distance (unless you gain more during your drive).\n")
time.sleep(2)

p = Adventure(player_name)
p.challenge(player_name)


# STRETCH GOALS:
# -- Add difficulty levels (add inputs to time, distance, etc that would make winning more difficult)
# -- Add choices (where would you like to travel to/from? if something happens, what would you like to do?)
# -- Add options if you run low on something. For example, if HEALTH is low, you can go through a drive-through, but would lose money. Or, if you are low on time, you can choose to drive faster, at the risk of getting pulled over (and would lose MONEY and TIME, or go to jail and lose the game)
# -- Add the option for more players, and whoever gets there first wins