import random





# Let's build a simple board game that runs on the terminal. We'll represent the board using a list of lists. We'll use two ints to represent that player's position on the board. Every iteration of the game loop, the user will be prompted for a command. Start with the code below, and add your own modifications.
#
# Possible modifications:

board_height = 10
board_width = 10

game_board = []
#creates the game board:
for i in range(board_height):
    game_board.append([])
    for j in range(board_width):
        game_board[i].append('')



# player postition
player_i = 4
player_j = 4
# enemey positions
for i in range(4):
    enemy_i = random.randint(0,board_height-1)
    enemy_j = random.randint(0,board_height-1)
    game_board[enemy_i][enemy_j] = '⚑'



# game starting


while True:

    command = input('what is your your move? ')  # get the command from the user
    #lists of commands
    left_list=['left','l','west',]
    right_list = ['right','r','east']
    down_list = ['down','d','south']
    up_list = ['up','u','north']
    if command == 'done':
        break  # exit the game
    elif command in left_list:
        player_j -= 1  # move left
    elif command in right_list:
        player_j += 1  # move right
    elif command in up_list:
        player_i -= 1  # move up
    elif command in down_list:
        player_i += 1  # move down

 #check if the player is on the same space as an enemy
    if game_board[player_i][player_j] == '⚑':
        print('you\'ve encountered an enemy!')
        user_choice = input('Quick,choose rock, paper, or scissors!')
        computer_choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(computer_choices)

        print(f'the enemy chose {computer_choice}')
        print(f'you chose {user_choice}')
        if user_choice == 'rock':
            if computer_choice == 'rock':
                print('Its a tie')
            if computer_choice == 'paper':
                print('enemy wins!')
            if computer_choice == 'scissors':
                print('user wins ! ')
                print('you\'ve slain the enemy')
                board[player_i][player_j] = ' '
        if user_choice == 'paper':
            if computer_choice == 'paper':
                print('Its a tie')
            if computer_choice == 'rock':
                print('user wins ! ')
                print('you\'ve slain the enemy')
                board[player_i][player_j] = ' '
            if computer_choice == 'scissors':
                print('Computer wins ! ')
        if user_choice == 'scissors':
            if computer_choice == 'scissors':
                print('Its a tie')
            if computer_choice == 'paper':
                print('User wins!')
                print('you\'ve slain the enemy')
                board[player_i][player_j] = ' '
            if computer_choice == 'rock':
                print('Computer wins ! ')

# printing out the board
    for i in range(board_height):
        for j in range(board_width):
            if i == player_i and j == player_j:
                print('x', end=' ')
            else:
                print(game_board[i][j], end=' ')
        print()
