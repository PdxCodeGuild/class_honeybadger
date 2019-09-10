from random import randint

def getRandomNumbers():
    ticket = []
    for i in range(6):
        ticket.append(randint(1,99))
    return ticket
    
def compTix(winning_tix, ticket):
    match = 0
    for i in range(0, 6):
        if (winning_tix[i] == ticket[i]):
            match += 1
        continue
    return match

win_amounts = [0, 4, 7, 100, 50000, 1000000, 250000000]

def main():
    balance = 0
    expences = 0
    winning_tix = getRandomNumbers()
    for i in range (100000):
        ticket = getRandomNumbers()
        num_matches = compTix(winning_tix, ticket)
        balance += win_amounts[num_matches]
        expences += 2
    print(f"Your balance is {balance}.\n Your expences are {expences}. \n Your ROI is {(balance - expences)/expences} ")

main()
