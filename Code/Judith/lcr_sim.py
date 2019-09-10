#filename: lcr_sim.py

import random

dot = '\u2022'
die = ['L', 'C', 'R', dot, dot, dot]

# players = [{
#     'name': 'mike',
#     'chips': 3
# },{
#     'name': 'nancy',
#     'chips': 3
# }]


players = [{'name': f'player {i}', 'chips': 3} for i in range(int(input('How many players?: ')))]
# players[2]['chips'] += 1 

# players = [{f'player: {i}': 3} for i in range(int(input('How many players?: ')))]
print(players)


def roll(int):
    roll = [random.choice(die) for i in range(int)]
    return roll
       
def game(players):
    
    pot = 0

    game_won = False
    
    while not game_won:
        for i in range(len(players)):
            player = players[i]            
            for result in roll(player['chips']):
                print(result)
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
                    game_won = True
                if play_again == 'y':
                    print('no.') #come back later.
                    game_won = True

                
        
        

game(players)

