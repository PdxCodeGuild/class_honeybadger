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

class Adventure:
    def __init__(self, player, health = 100, money = 100, distance = 10, time = 60, sleep = 2):
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
            print_sleep(f"\n{choose_event['text']}.\n  --> Your HEALTH is {plus_minus} by {abs(choose_event['health'])}.")
            self.health += choose_event["health"]
            time.sleep(self.sleep)
    
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
            print_sleep(f"\n{choose_event['text']}.\n  --> You {plus_minus} ${abs(choose_event['money'])}.")
            self.money += choose_event["money"]    
            time.sleep(self.sleep)
    
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
            print_sleep(f"\n{choose_event['text']}.\n  --> Your DISTANCE is {plus_minus}")
            self.distance += choose_event["distance"]
            time.sleep(self.sleep)
    
    def time(self):
        if_play = random.choice([True, False])
        if if_play:
            neg_num = random.randint(-2, 0)
            pos_num = random.randint(1, 3)
            events = [
                {"text" : "You're driving behind someone who refuses to go faster than five miles under the speed limit", "time" : neg_num, "ascii" : ascii_art.car},
                {"text" : "You discovered your clock was set wrong", "time" : pos_num, "ascii" : ascii_art.car},
                {"text" : "You saw a puppy and stopped your car to go pet it", "time" : pos_num, "ascii" : ascii_art.dog},
                {"text" : "It started to rain and everyone is driving slowly", "time" : neg_num, "ascii" : ascii_art.car},
                {"text" : "The bridge is up", "time" : neg_num, "ascii" : ascii_art.bridge}
                ]
            choose_event = random.choice(events)
            if choose_event["time"] < 0:
                plus_minus = "lose"
            elif choose_event["time"] == 0:
                plus_minus = "(amazingly) unchanged."
            else:
                plus_minus = "get an extra"
            print_ascii(f"\n{choose_event['ascii']}\n")
            print_sleep(f"\n{choose_event['text']}.\n  --> You {plus_minus} {abs(choose_event['time'])} minutes.")
            self.time += choose_event["time"]
            time.sleep(self.sleep)
    
    def death(self):
        death_event = random.randint(1, 100)
        death_event_2 = random.randint(1, 100)
        if death_event == death_event_2:
            print_ascii(ascii_art.rip)
            print_sleep("There was a massive earthquake and you fell into lava throuh a fissure in the pavement. You're now dead.\nGAME OVER")
            exit()

    def problem(self):
        problem = random.choice(["health", "money", "time"])
        return problem
    
    def challenge(self, player):
        time.sleep(self.sleep)
        keep_playing = "yes"
        while self.health > 0 and self.money > 0 and self.time > 0:
            while keep_playing == "yes":
                Adventure.health(self)
                Adventure.money(self)
                Adventure.distance(self)
                Adventure.death(self)
                Adventure.time(self)
                self.time -= 5
                self.distance -= 1
                status = f"\n\n* * * * * * * * * * * * * * *\n* * * * * * * * * * * * * * *\n\n{self.player}'s Status:\n\tHealth = {self.health}\n\tMoney = ${self.money} \n\t{self.time} minutes remaining\n\t{self.distance} miles to your destination\n\n* * * * * * * * * * * * * * *\n* * * * * * * * * * * * * * *\n\n"
                print_fast(status)
                keep_playing = input("Would you like to continue to your destination?\t").lower()
                if self.health == 0:
                    print_ascii(ascii_art.rip)
                    print("You died.")
                    break
                elif self.money == 0:
                    print_fast("You ran out of money.\n")
                    exit()
                elif self.time == 0:
                    print_fast("You didn't get there in time.\n")
                    exit()
                elif self.distance == 0:
                    print_fast("You made it to your destination!\n")
                    exit()
                elif keep_playing != "yes":
                    print_ascii(ascii_art.tent)
                    print_fast("\n\nYou gave up and moved into a tent on the side of the road.\n\n")
                    exit()
                else:
                    continue
            

player_name = input("\nWhat is your name? ")
print_fast(f"\nHello, {player_name}, and welcome to \"The Portland Trail\"!")
time.sleep(.5)
print_fast("\n\nLet's see if you can drive your way through Portland to your destination before you run out of money, time, or you die.\n")

p = Adventure(player_name)
p.challenge(player_name)