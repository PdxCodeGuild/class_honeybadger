


import random


# a = 'hello'
# # b = a
# b = 'hell'
# b += 'o'

# a = not True
# b = not (5 == 5)
# a = not a
# b = not b
# 
# print(a, id(a))
# print(b, id(b))
# 
# print(f'a is b {a is b}')
# print(f'a == b {a == b}')
# exit()







# players = [('Mike', 3), ('Nancy', 3), ('Joe', 3)]
# players[0][1] += 1 # crash
# players[0] = (players[0][0], players[0][1]+1) # tedious
# 




def roll_die():
    return random.choice(['L', 'C', 'R', '.', '.', '.'])


# players = []
# while True:
#     name = input('enter a player name: ')
#     if name == 'done':
#         break
#     players.append({
#         'name': name,
#         'chips': 3,
#         'games_won': 0
#     })

players = [{
    'name': 'Jill',
    'chips': 3,
    'games_won': 0
},{
    'name': 'Jane',
    'chips': 3,
    'games_won': 0
},{
    'name': 'Joe',
    'chips': 3,
    'games_won': 0
}]




# play_game = True
# while play_game:
#     for i in range(len(players)):
#         player = players[i]
# 
#         play_game = False
#         break


games_to_play = int(input('how many games would you like to play? '))

play_game = True
current_player_index = 0
pot = 0
while games_to_play > 0:
    player = players[current_player_index]
    left_player  = players[len(players)-1 if current_player_index == 0 else current_player_index-1]
    right_player = players[0 if current_player_index == len(players)-1 else current_player_index+1]
    
    # left_player = None
    # if current_player_index == 0:
    #     left_player = players[len(players)-1]
    # else:
    #     left_player = players[current_player-1]
    # 
    # right_player = None
    # if current_player_index == len(players)-1:
    #     right_player = players[0]
    # else:
    #     right_player = players[current_player_index+1]
    
    
    
    die_rolls = 3 if player['chips'] >= 3 else player['chips']
    # die_rolls = 3
    # if player['chips'] < 3:
    #     die_rolls = player['chips']
    
    for i in range(die_rolls):
        die = roll_die()
        
        if die == 'L':
            player['chips'] -= 1
            left_player['chips'] += 1
        elif die == 'R':
            player['chips'] -= 1
            right_player['chips'] += 1
        elif die == 'C':
            player['chips'] -= 1
            pot += 1
    
    
    for player in players:
        if player['chips'] + pot == 3*len(players):
            print(player['name'] + ' won')
            player['games_won'] += 1
            
            # reset the game state
            for p in players:
                p['chips'] = 3
            pot = 0
            
            games_to_play -= 1
            break
            
            
    
    
    
    current_player_index = (current_player_index+1) % len(players)
    
    # current_player_index += 1
    # if current_player_index == len(players):
    #     current_player_index = 0
    


for player in players:
    print(player['name'] + '\t' + str(player['games_won']))





