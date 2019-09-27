# #filename: blackjack.py

# import random

# cards = ('A','2','3','4','5','6','7','8','9','J','Q','K')

# dlrHand = [random.choice(cards) for i in range(2)]
# plyrHand = [random.choice(cards) for i in range(2)]

# print(plyrHand,dlrHand)

# def count(hand):
#     count = 0
#     for card in hand:
#         if card in ['J','Q','K']: card = 10 
#         if card in ['2','3','4','5','6','7','8','9']: card = int(card) 
#         if card == 'A':
#             if count < 11: card = 11
#             else: card = 1
#         count += card
#     return count

# def action(count,hand):
#     if count >= 17:
#         pass
#     if count == 11:
#         #doubledown
#         hand.append(random.choice(cards))
#     if count <= 10:
#         hand.append(random.choice(cards))
#     return hand

# def round(plyrHand,dlrHand,action):
#     finPlyrHand = action(count(plyrHand),plyrHand)
#     finDlrHand = action(count(dlrHand),dlrHand)
#     print(finPlyrHand,finDlrHand)
#     if finPlyrHand > finDlrHand:
#         return True


# if round(plyrHand,dlrHand,action):
#     print('win!')
# else: print('lose...')

###############################################
##############  class method  #################
###############################################

import random


class Players:
    def __init__(self, name, hand = [], chips = 20):
        self.name = name
        self.hand = hand
        self.chips = chips
    
    def __str__(self):
        return f'{self.name}, {self.hand}, {self.chips}'
    
    __repr__ = __str__

class Deck:
    def __init__(self, players):
        self.cards = ['A','2','3','4','5','6','7','8','9','J','Q','K'] * 4
        self.players = players

    def __str__(self):
        return f'{self.cards}'
    
    def deal(self, cards, players):
        for player in players:
            for i in range(2):
                top = random.choice(cards)
                player.hand.append(top)
                cards.remove(top)

    def count(self, players, index):
        cards = players[index][1]
        count = 0
        for card in cards:
            if card in ['J','Q','K']: card = 10 
            if card in ['2','3','4','5','6','7','8','9']: card = int(card) 
            if card == 'A':
                if count < 11: 
                    card = 11
                else: card = 1
            count += card
        return count



        



players = [Players(input(f'player {i}, input your name: ')) for i in range(int(input('How many players?...')))]
game = Deck(players)
game.deal(game.cards, players)
print(players)
print(game.count(players, 0))


