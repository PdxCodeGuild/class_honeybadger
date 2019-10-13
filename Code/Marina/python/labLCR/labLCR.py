import random

list_of_players = []
def player_list():
    while True:
        player = input("What is your name, or type 'done' when there are no more players: ")
        if player != 'done':
            print(player)
            list_of_players.append({
                'name': player,
                'chips': 1
            })
            print(list_of_players)
        else:
            print(list_of_players)
            return list_of_players


# players = player_list()
players = [{'name': 'w', 'chips': 3}, {'name': 'e', 'chips': 3}]


def roll_die():
    die = {
    1 : '.',
    2 : '.',
    3 : '.',
    # pass the chip to the right
    4 : 'r',
    # pass the chip to pot
    5 : 'c',
    # pass the chip to the left
    6 : 'l'
    }
    # print(die)

    roll = random.randint(1, 6)
    return die[roll]


pot = 0
for i in range(len(players)):
    print(players[i]['name'] + "'s turn")
    num_die = 3
    if players[i]['chips'] < 3:
        num_die = players[i]['chips']
    for j in range(num_die):

        roll = roll_die()
        print('rolled a ' + roll)
        if roll == 'l':
            pass
            # decrement the current player's chips
            # increment the left player's chips
        elif roll == 'c':
            pass
            # decrement the current player's chips
            # increment the pot

    # if roll <= 3:
    #     print(f" {player} rolls a {roll}")
    # if die.keys() == 1 or die.keys() == 2 or die.keys() == 3:
    #     print(die.value())
    #     pot +=1

print(pot)
