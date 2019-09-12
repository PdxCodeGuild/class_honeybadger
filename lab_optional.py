import random




# dicts_list = [
#   {'player_1': 3,},
#   {'player_2': 3,},
#   {'player_3': 3,},
#   {'pot': 0}
#     ]
def roll_dice():
    dice_choices = ['l','c','r','.','.','.']
    return random.choice(dice_choices)


def play_game(adict):
    pot = 0
    for i in range(len(players)):
        print(f'{players[i]["name"]}\'s turn')
        dice_choices = roll_dice()

        if dice_choices == 'l':
            print('\trolled an l')
            players[i]['chips'] -= 1
            players[i-1]['chips'] += 1

        if dice_choices == 'r':
            print('\trolled an r')
            players[i]['chips'] -= 1
            if i == len(players)-1:
                players[0]['chips'] += 1
            else:
                players[i+1]['chips'] += 1

        if dice_choices == 'c':
            print('\trolled an c')
            pot += 1
        if dice_choices == '.':
            print('\trolled a .')

    print(players)
    print(f'the pot is: {pot}')




players = [{
    'name': 'mike',
    'chips': 3
},{
    'name': 'joe',
    'chips': 3
},{
    'name': 'matt',
    'chips': 3
}]
# print(players)
play_game(players)








# fruits = []
# x = 0
#
# def example():
#     fruits.append('apple')
#     x = x + 1
#
# example()
# print(fruits)
# print(x)
