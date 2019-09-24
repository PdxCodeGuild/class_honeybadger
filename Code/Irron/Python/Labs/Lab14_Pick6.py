'''
Lab 14: Pick6

Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and 
payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. 
Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. 
Calculate your net winnings (the sum of all expenses and earnings).

    a ticket costs $2
    if 1 number matches, you win $4
    if 2 numbers match, you win $7
    if 3 numbers match, you win $100
    if 4 numbers match, you win $50,000
    if 5 numbers match, you win $1,000,000
    if 6 numbers match, you win $25,000,000

One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both 
the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches 
between the winning numbers and the ticket.

Steps:

    1. Generate a list of 6 random numbers representing the winning tickets
    2. Start your balance at 0
    3. Loop 100,000 times, for each loop:
    4. Generate a list of 6 random numbers representing the ticket
    5. Subtract 2 from your balance (you bought a ticket)
    6. Find how many numbers match
    7. Add to your balance the winnings from your matches
    8. After the loop, print the final balance

Version 2

The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings 
and expenses.
'''

import random

def pick6():
    ticket = [random.randint(1,100) for i in range(6)] #--->list comprehension to create a list of 6 random numbers 
    
    #print(ticket)
    return ticket

def calc_number_matches(winning, player):
    winning_tix = []
    player_tix = []
    matches = 0

    #appending list of random numbers for winning and player tix
    for i in range(len(winning)):
        winning_tix.append(winning[i])
                
    for i in range(len(player)):
        player_tix.append(player[i])
    print(winning_tix, player_tix)

    no_matches = 0

    for i in range(len(winning_tix)):
        for j in range(len(winning_tix)):
            if winning_tix[i] == player_tix[j]:
                no_matches +=1
                #print('match')
                print(f'Congrats! You have {no_matches} matching number(s).')
    return no_matches
   

# def calc_number_plays():
#     for i in range(10):


#Need to create loop to run 10,000 times.  Will while loop work? Pass the no matches and number of tix purchased, should equal 10k
def calc_earning(no_matches):
    #wins    1  2   3     4     5         6
    table = [4, 7, 100, 50000, 1000000, 25000000]
    no_mathces = []
    
    
    winnings = #use index of #wins to return earnings
     
    ticket_cost = 2
    number_plays = 2
    balance = 0
    earnings = 0
    total_spent = ticket_cost * number_plays
    earnings = table

    
    


#Calling Functions 
winning_tix = pick6()
player_tix = pick6()
calc_number_matches(winning_tix, player_tix) #---> calling pick6 2x to generate a winning tix and player ticket and passing both to function




#Test code, checking if numbers and index == match
# winning_ticket = [5, 10, 2, 1, 1] 
# ticket = [5, 5, 35, 2, 1]

# for item in range(len(winning_ticket)):
#     for item1 in range(len(winning_ticket)):
#         if winning_ticket[item] == ticket[item1]:
#             # if winning_ticket.index(winning_ticket[item]) == ticket.index(ticket[item1]):

#                 print(winning_ticket[item])
#         else:
#             print('no match')

 #if winning_ticket[item] == ticket[item1]: #--->, finds matches but does not consider positionings
 #if winning_ticket[item] == ticket[item1] and winning_ticket.index(winning_ticket[item]) == ticket.index(ticket[item1]):
