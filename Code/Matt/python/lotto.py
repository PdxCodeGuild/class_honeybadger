# #
# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
# #
import random

balance = 0


# creates a list of 6 random numbers
def number_generator():
    return [random.randint(1,100) for i in range(6)]

# compares the indecies of each list.
def num_matches(user_tickets, winning_numbers):
    total_matches = 0
    for i in range(len(user_tickets)):
       if user_tickets[i] == winning_numbers[i]:
            total_matches += 1
    return total_matches
       # elif user_tickets[i] != winning_numbers[i]:
       #      continue


# nums = [4, 5, 6, 10, 2, 11]
# nums_less_than_10 = []
# for num in nums:
#     if num >= 10:
#         continue
#     nums_less_than_10.append(num)



winning_numbers = number_generator()
total_matches = 0

print(winning_numbers)

for i in range(25):
    user_tickets = number_generator()
    total_matches = 0
    num_matches(user_tickets,winning_numbers)
    print(f'{winning_numbers} {user_tickets} {total_matches}')

def total_amount_won():
    if total_matches == 1:
        print("You win $4")
    elif total_matches == 2:
        print("You win $7")
    elif total_matches == 3:
        print("You won ")
print (total_amount_won())
