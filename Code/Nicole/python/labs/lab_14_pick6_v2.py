# pick6.py

from random import choice

# define function

def winning_amount(winner):
    balance = 0
    if winner == 1:
        balance += 4
    elif winner == 2:
        balance += 7
    elif winner == 3:
        balance += 100
    elif winner == 4:
        balance += 50000
    elif winner == 5:
        balance += 1000000
    elif winner == 6:
        balance += 25000000
    else:
        balance += 0
    return balance
        
numbers = []
number_pick = list(range(1, 100))
balance = 0
loop = 0
winner = 0
total_balance = 0

# pick winning numbers

winning_ticket = []

for number in range(1,7):
    winning_ticket.append(choice(number_pick))

print(f"\nThe winning ticket numbers are: {winning_ticket}\n")

while loop <= 10001:
    purchased_ticket = []
    for number in range(1,7):
        purchased_ticket.append(choice(number_pick))
    ticket_index = 0
    while ticket_index <= 5:
        if winning_ticket[ticket_index] == purchased_ticket[ticket_index]:
            winner += 1
        else:
            winner += 0
        ticket_index += 1
    loop += 1
    # print(winner)
    total_balance += winning_amount(winner)

roi = (total_balance-200000)/200000

print(f"\nYou won ${total_balance}\n")
print(f"Your ROI is {roi}\n")