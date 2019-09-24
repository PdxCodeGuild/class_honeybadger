# filename: lab26_daemon_maze.py

# text based adventure game, the goal is to defeat the demon in an encounter
# to do so you must navigate the demons lair, gathering items to assist you
# and avoiding traps, enemies, and the demon itself until you are ready to face it

import random

class Board:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[['x']for j in range(self.width)] for i in range(self.height)]
        

    def print(self, entities):
        printable = ''
        
        for i in range(self.height): # sets entities
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].loc_i == i and entities[k].loc_j == j:
                        self.board[i][j].append(entities[k].character)
        
        for i in range(self.height-1): # renders board
            printable += f'{self.board[i]} \n'
        printable += f'{self.board[self.height-1]}'
        
        print(printable)
    
    def random_loc(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

class Entity:

    def __init__(self, character, loc_i, loc_j):
        self.character = character
        self.loc_i = loc_i
        self.loc_j = loc_j

        

board = Board(3, 3)
chara = Entity('$', 1, 1)
entities = [chara]

board.print(entities)

    
                

