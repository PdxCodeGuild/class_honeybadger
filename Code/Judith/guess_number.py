#filename: guess_number.py

import random

#Global variables
numbrs=[1,2,3,4,5,6,7,8,9,10]

pcatk=random.choice(numbrs)
usratk=int()
round=1

#test
print("Let's begin!")

#base loop
while round<10000:

    #counter
    if round==1:
        print("first round! ",round)
    elif round<11:
        print("round ",round)
    else:
        print("You've used all your guesses, game over!")
        break

    #round up
    round+=1

    #input validation and comparison
    try:
        usratk=int(input("Please enter a number between 1 and 10\n"))
        if not 1<=usratk<=10:
            print("Between 1 and 10, Please")
        elif usratk>pcatk:
            print("Too High!")
        elif usratk<pcatk:
            print("Too Low!")
        elif usratk==pcatk:
            print("You win!")
            break
    except ValueError:
        print("Invalid input")
else:
    print("wtf")
