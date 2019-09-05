import random

inputted_grade = input("What is your numeric grade? ")

if inputted_grade.isdigit():
    print(f"Your numeric grade is: {inputted_grade}")
    user_grade = int(inputted_grade)

    remainder = user_grade % 10

    if 90 <= user_grade <= 100:
        if 1 <= remainder <= 5:
            print("You got an A-!")
        elif 6 <= remainder <= 9:
            print("You got an A+")
    elif 80 <= user_grade <= 89:
        if 1 <= remainder <= 5:
            print("You got a B-")
        elif 6 <= remainder <= 9:
            print("You got a B+")
    elif 70 <= user_grade <= 79:
        if 1 <= remainder <= 5:
            print("You got a C-")
        elif 6 <= remainder <= 9:
            print("You got a C-")
    elif 60 <= user_grade <= 69:
        if 1 <= remainder <= 5:
            print("You got a D-")
        elif 6 <= remainder <= 9:
            print("You got a D+")
    else:
        print("You got an F")
else:
    print("Please enter a real number!")

rival_score = random.randint(0, 100)
print(f"Your rival scored {rival_score} ")
if user_grade > rival_score:
    print("You beat your rival!")
else:
    print("You lost, looser! She beat you!")
