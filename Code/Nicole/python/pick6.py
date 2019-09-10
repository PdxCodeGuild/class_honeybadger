# pick6.py

from random import choice

# define function

def winning_amount(match):
    balance = 0
    if match == 1:
        balance += 4
    elif match == 2:
        balance += 7
    elif match == 3:
        balance += 100
    elif match == 4:
        balance += 50000
    elif match == 5:
        balance += 1000000
    elif match == 6:
        balance += 25000000
    else:
        balance += 0
    return balance
        
match_list = list(range(1,5))
balance_list = [1, 7, 100, 5000, 1000000, 25000000]
number_pick = list(range(1, 100))
balance = 0
loop = 0
match = 0
total_balance = 0

# pick winning numbers

winning_ticket = []

for number in range(6):
    winning_ticket.append(choice(number_pick))

# print(f"\nThe winning ticket numbers are: {winning_ticket}\n")

while loop <= 100001:
    purchased_ticket = []
    for number in range(6):
        purchased_ticket.append(choice(number_pick))
    for i in range(6):
        if winning_ticket[i] == purchased_ticket[i]:
            match += 1
    loop += 1
    total_balance += winning_amount(match)
    total_balance -= 2

# print(f"\nYou won ${total_balance}\n")
print("\nYou won ${:,}".format(total_balance))
print("\n")