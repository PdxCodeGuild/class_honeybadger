# lab_optional_lcr.py

import random

def lcr():
    player_1 = input("Player 1, please enter your name: ")
    player_2 = input("Player 2, please enter your name: ")
    player_3 = input("Player 3, please enter your name: ")
    player_dict = {
        player_1 : 3, 
        player_2 : 3, 
        player_3 : 3
        }
    dice = {
        1 : "dot",
        2 : "dot",
        3 : "dot",
        4 : "l",
        5 : "c",
        6 : "r",
        }
    game_play = True
    

    pot = 0
    
    while game_play is True:
        for x in player_dict:
            if player_dict[x] > 3:
                plays = 3
            else:
                plays = player_dict[x]
            while plays > 0:
                           
                print(f"It's {x}'s turn #{plays}")
                plays -= 1 
                y = random.randint(1,6)
                print(f"{x} rolled a {dice[y]}")
                if dice[y] == "dot":
                    continue
                elif dice[y] == "l":
                    if x == player_1:
                        print(f"{x} started with {player_dict[x]} chips")
                        player_dict[x] -= 1
                        player_dict[player_2] += 1
                        print(f"{x} now has {player_dict[x]} chips")
                    elif x == player_2:
                        print(f"{x} started with {player_dict[x]} chips")
                        player_dict[x] -= 1
                        player_dict[player_3] += 1
                        print(f"{x} now has {player_dict[x]} chips")
                    elif x == player_3:
                        print(f"{x} started with {player_dict[x]} chips")
                        player_dict[x] -= 1
                        player_dict[player_1] += 1
                        print(f"{x} now has {player_dict[x]} chips")
                elif dice[y] == "r":
                    if x == player_1:
                        print(f"{x} started with {player_dict[x]} chips")
                        player_dict[x] -= 1
                        player_dict[player_3] += 1
                        print(f"{x} now has {player_dict[x]} chips")
                    elif x == player_2:
                        print(f"{x} started with {player_dict[x]} chips")
                        player_dict[x] -= 1
                        player_dict[player_1] += 1
                        print(f"{x} now has {player_dict[x]} chips")
                    elif x == player_3:
                        print(f"{x} started with {player_dict[x]} chips")
                        player_dict[x] -= 1
                        player_dict[player_2] += 1
                        print(f"{x} now has {player_dict[x]} chips")
                elif dice[y] == "c":
                    print(f"The pot started with {pot} chips")
                    player_dict[x] -= 1
                    pot += 1
                    print(f"The pot now has {pot} chips")
                print(f"\nPlayer {x} plus the pot is {player_dict[x] + pot} chips")
                
                
                # exit()
                
            if player_dict[x] + pot == 9:
                print(f"{x} is the winner!")
                again = input("\nWould you like to play again? ")
                if again == "no":
                    print("Thanks for playing!")
                    game_play = False
                    break
                else:
                    player_dict = {
                        player_1 : 3, 
                        player_2 : 3, 
                        player_3 : 3
                        }
                    pot = 0


lcr()