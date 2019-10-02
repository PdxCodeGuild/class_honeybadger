# pick6 game
import random

def create_ticket():
    user_numbers = []
    for i in range(6):
        user_numbers.append(random.randint(1, 99))
    return user_numbers

winning_ticket = create_ticket()
ticket = create_ticket()

print (winning_ticket)
print(ticket)

def formula(ticket, winning_ticket):

    match = 0
    for i in range(6):
        if ticket[i] == winning_ticket[i]:
            matches += 1
            reward = [4, 7, 100, 1000000, 25000000]
    return reward[matches]

# def program():
#     winnings = create_ticket()
#     earnings = 0
#     expenses = 0
#     for i in range(100000):
#         ticket = create_ticket()
#         expenses += 2
#         earnings += formula(ticket, winnings)
#     balance = earnings-expenses
#     print(balance)
