import random



print("Welcome to Rock Paper Scissors!")



def one_player():

    user_score = 0
    cpu_score = 0
    round = 1
    play_again = "yes"
    choices = ["rock", "paper", "scissors"]


    #puting all scenarios into three lists
    tie_outcomes = ["rock vs rock",  "scissors vs scissors", "paper vs paper"]
    user_wins = ["taco vs scissors", "taco vs rock", "taco vs paper", "rock vs scissors", "paper vs rock", "scissors vs paper"]
    cpu_win = ["rock vs paper", "scissors vs rock", "paper vs scissors"]

    while play_again == "yes":

        user_choice = input("Rock, paper, or scissors? ").lower()
        cpu_choice = random.choice(choices)

        outcome = user_choice + " vs " + cpu_choice
        print(outcome)

        if outcome in tie_outcomes:
            print("IT'S A TIE")
            user_score += 0
            cpu_score += 0
        elif outcome in user_wins:
            user_score += 2
            cpu_score -= 1
            print("You Won!!")
        elif outcome in cpu_win:
            cpu_score += 2
            user_score -= 1
            print("Oof! you lost")

        else:
            print("Please enter rock, paper or scissors.")
        play_again = input("Would you like to play again? yes/no ").lower()

        print(f"Current Score: User Score: {user_score}, CPU Score: {cpu_score}")



        while play_again not in ["yes", "no"]:
            play_again = input("Do you want to play again? (yes/no) ").lower()

    else:
        print(f'Final User Score: {user_score}')
        print(f'Final CPU Score {cpu_score}')
        print("Come back soon!")

def two_player():
    user_choice = input("Rock, paper, or scissors? ").lower()
    user_two_choice = input("Rock, paper, or scissors? ").lower()

    tie_outcomes = ["rock vs rock",  "scissors vs scissors", "paper vs paper"]
    user_wins = ["rock vs scissors", "paper vs rock", "scissors vs paper"]
    user_two_win = ["rock vs scissors", "scissors vs paper", "paper vs rock"]


    outcome = user_choice + " vs " + user_two_choice
    print(outcome)

    if outcome in tie_outcomes:
        print("IT'S A TIE")
        user_score += 0
        user_two_score += 0
    elif outcome in user_wins:
        user_score += 2
        user_two_score -= 1
        print("User 1 Wins!")
    elif outcome in user_two_win:
        user_two_score += 2
        user_score -= 1
        print("User 2 Wins!")

    else:
        print("Please enter rock, paper or scissors.")
    play_again = input("Would you like to play again? yes/no ").lower()

    print(f"Current Score: User Score: {user_score}, User 2 Score: {user_two_score}")



    while play_again not in ["yes", "no"]:
        play_again = input("Do you want to play again? (yes/no) ").lower()

    else:
        # print(f'Final User Score: {user_score}')
        # print(f'Final User 2 Score {user_two_score}')
        print("Come back soon!")

main_input = input("How many players?")
if main_input == "1":
    one_player()
else:
    two_player()
