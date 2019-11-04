import random



game_in_session = 'yes'
while game_in_session != 'done':
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)

    user_choice = input('Enter your choice (rock, paper , or scissors: )')

    print(f'the computer chose {computer_choice}')
    print(f'you chose {user_choice}')
    if user_choice == 'rock':
        if computer_choice == 'rock':
            print('Its a tie')
        if computer_choice == 'paper':
            print('User wins!')
        if computer_choice == 'scissors':
            print('Computer wins ! ')
    if user_choice == 'paper':
        if computer_choice == 'paper':
            print('Its a tie')
        if computer_choice == 'rock':
            print('User wins!')
        if computer_choice == 'scissors':
            print('Computer wins ! ')
    if user_choice == 'scissors':
        if computer_choice == 'scissors':
            print('Its a tie')
        if computer_choice == 'paper':
            print('User wins!')
        if computer_choice == 'rock':
            print('Computer wins ! ')
    game_in_session = int(input(f'Do you want to keep playing if your done, type "done":')
