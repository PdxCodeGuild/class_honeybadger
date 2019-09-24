'''
Lab 7: Rock Paper Scissors

Let's play rock-paper-scissors with the computer.

    The computer will ask the user for their choice (rock, paper, scissors)
    The computer will randomly choose rock, paper or scissors
    Determine who won and tell the user

Let's list all the cases:

    rock vs rock (tie)
    rock vs paper
    rock vs scissors
    paper vs rock
    paper vs paper (tie)
    paper vs scissors
    scissors vs rock
    scissors vs paper
    scissors vs scissors (tie)

'''
import random  
def game(computer, player):
       
    if computer == player:
        print('We have a tie!')
    
    #focus on plays where computer wins.  All other combinations, Player wins, reflected in Else statement
    elif computer == 'paper' and player == 'rock':
        print('Computer Wins!')
    elif computer == 'rock' and player == 'scissors':
        print('Computer Wins!')
    elif computer == 'paper' and player == 'scissors':
        print('Computer Wins!')
    else:
        print('Player Wins!')

options = ['rock', 'paper', 'scissors']   
user_input = input('Please choose rock, scissors or paper ')
random_computer = random.choice(options)

print(f'You chose {user_input}')
print(f'Your competitor chose {random_computer}')

game(random_computer,user_input)
