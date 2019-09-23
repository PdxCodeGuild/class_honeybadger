import random

class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character

class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '$')

class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '*')

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def random_location(self):
    return random.randint(0, self.width -1), random.randint(0, self.height -1)

def __getitem__(self, j):
    return self.board[j]

def print(self, entities):
    for i in range(self.height):
        for j in range(self.width):
            for k in range(len(entities)):
                if entities[k].location_i == i and entities[k].location_j == j:
                    print(entities[k].character, end='')
                    break
            else:
                print(' ', end='')
            print()

board = Board(3,3)

pi, pj = board.random_location()
player = Player(pi, pj)

entities = [player]
enemies = []

for i in range(3):
    ei, ej = board.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)

while True:

    board.print(entities)

    command = input('what is your command? ')

    if command == 'done':
        break
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1
    elif command in ['u', 'up', 'n', 'north']:
        player.location_i -= 1
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += 1

    for enemy in enemies:
        if enemy.location_i == player.location_i and enemy.location_j == player.location_j:
            print('enemy at the gate!')
            action = input('what do you wish to do? ')
            if action == 'attack':
                print('enemy is dead')
                entities.remove(enemy)
                enemies.remove(enemy)
                break
            else:
                print('you are dead')
                exit()
