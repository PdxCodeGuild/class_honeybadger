#filename: lcr_sim.py

import random

dot = '\u2022'
die = ['L', 'C', 'R', dot, dot, dot]

def roll(int):
    roll = [random.choice(die) for i in range(int)]
    return roll
       
def game():
    
    players = [{'name': f'player {i}', 'chips': 3} for i in range(int(input('How many players?: ')))]

    pot = 0

    game_over = False
    
    while not game_over:
        for i in range(len(players)):
            player = players[i]
            reslist = []            
            for result in roll(player['chips'] if player['chips'] <= 3 else 3):
                reslist.append(result)
                if result == 'L':
                    player['chips'] -= 1
                    players[i+1 if i+1 < len(players) else 0]['chips'] += 1
                if result == 'R':
                    player['chips'] -= 1
                    players[i-1]['chips'] += 1
                if result == 'C':
                    player['chips'] -= 1
                    pot += 1
                if result == dot:
                    continue
            print(player, reslist)
            if player['chips'] + pot == len(players) * 3:
                player['chips'] += pot
                prize = player['chips']
                winner = player['name']
                print(f'{winner} wins the round...')
                play_again = input('play again? y or n: ')
                while play_again not in ['y','n']:
                    play_again = input('play again? y or n: ')
                if play_again == 'n':
                    print(f'Game ended, {winner} leaves with {prize} chips!')
                    game_over = True
                if play_again == 'y':
                    pot = 0
                    players = [{'name': f'player {i}', 'chips': 3} for i in range(int(input('How many players?: '))-1)]
                    players.append({'name': 'player: X', 'chips': prize})
                    print('winner becomes player: X and starts with all their winnings from the previous game')
                    print(players)
                    break


                
        
        

game()

