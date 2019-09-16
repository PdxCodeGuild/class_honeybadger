# lab_07_rock_paper_scissors.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab07-rock_paper_scissors.md

import random

def rock_paper_scissors():
    game = ["rock", "paper", "scissors"]
    
    
    
    in_play = True
    
    while in_play:
        user_turn = input("Choose one: 'rock', 'paper', or 'scissors': ")
        computer_turn = random.choice(game)
        print(user_turn)
        print(computer_turn)        
    
    pass


rock_paper_scissors()