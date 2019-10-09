# filename: lab26_daemon_maze.py

# text based adventure game, the goal is to defeat the demon in an encounter
# to do so you must navigate the demons lair, gathering items to assist you
# and avoiding traps, enemies, and the demon itself until you are ready to face it

import random

class Board:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rooms = [[['0']for j in range(self.width)] for i in range(self.height)]
        self.entities = []
        
    def labrynth(self):
        labrynth = []
        passages = self.width + (self.width + 1)
        corridors = self.height + (self.height + 1)
        
        for i in range(corridors):
            if i == 0 or i == corridors - 1: # top and bottom walls, always closed
                labrynth.append([['X'] for i in range(passages)])
            elif i % 2 == 0: # walls inbetween floors
                passage = []
                for j in range(passages):
                    if j == 0 or j == passages: # first and last column always closed
                        passage.append(['X'])
                    elif j % 2 == 1: # walls to left, right, up, down of rooms may be open
                        passage.append([random.choice(['I', 'I', 'I', 'X'])])
                    else:
                        passage.append(['X'])
                labrynth.append(passage)

                    
            else:   # corridor contains rooms
                passage = []
                for j in range(passages):
                    if j == 0 or j == passages: # first and last column always closed
                        passage.append(['X'])
                    elif j % 2 == 0: # middle columns may be open
                        passage.append([random.choice(['I', 'I', 'I', 'X'])])
                    else: # rooms added here
                        passage.append(self.rooms[(i-1)//2][(j-1)//2])
                labrynth.append(passage)

        

        self.height = corridors
        self.width = passages
        self.rooms = labrynth
        # for i in range(len(self.rooms)):
        #     print(self.rooms[i], '\n')




    def print(self):
        printable = ''
        
        for i in range(self.height): # sets entities
            for j in range(self.width):
                for k in range(len(self.entities)):
                    if self.entities[k].character in self.rooms[i][j] and (self.entities[k].loc_i != i or self.entities[k].loc_j != j):
                        self.rooms[i][j].remove(self.entities[k].character)
                    if self.entities[k].loc_i == i and self.entities[k].loc_j == j and self.entities[k].character not in self.rooms[i][j]:
                        self.rooms[i][j].append(self.entities[k].character)
                    
                        
        
        for i in range(len(self.rooms) - 1): # renders board
            printable += f'{self.rooms[i]} \n'
        printable += f'{self.rooms[len(self.rooms) - 1]}'
        
        print(printable)
    
    def random_loc(self):
        return {'i': random.randint(0, (self.height//2) -1), 'j': random.randint(0, (self.width//2) -1)}
       

class Entity:

    def __init__(self, character, name):
        spawn_room = board.random_loc()
        self.loc_i = spawn_room['i']
        self.loc_j = spawn_room['j']
        self.character = str(character)
        self.loc_i = (self.loc_i * 2) + 1
        self.loc_j = (self.loc_j * 2) + 1
        self.name = name
        self.current_loc = [self.loc_i, self.loc_j]
        board.entities.append(self)


        

class Player(Entity):
    def __init__(self, name):
        super().__init__('$', name)
        self.inventory = []

    def move(self, command):
        if command == 'done': # initial move into 'wall' space
            pass
        elif command in ['l', 'left', 'w', 'west']:
            self.loc_j -= 1  # move left
        elif command in ['r', 'right', 'e', 'east']:
            self.loc_j += 1  # move right
        elif command in ['u', 'up', 'n', 'north']:
            self.loc_i -= 1  # move up
        elif command in ['d', 'down', 's', 'south']:
            self.loc_i += 1 # move down
        if not self.valid_move(): # check if wall is open
            print('you ran into a wall...')
        else: # push to space behind wall if open
            if command in ['l', 'left', 'w', 'west']:
                self.loc_j -= 1 
            elif command in ['r', 'right', 'e', 'east']:
                self.loc_j += 1  
            elif command in ['u', 'up', 'n', 'north']:
                self.loc_i -= 1  
            elif command in ['d', 'down', 's', 'south']:
                self.loc_i += 1 

        self.current_loc = [self.loc_i, self.loc_j] #set current_loc at end of function to avoid missed encounter
        return (self.loc_i, self.loc_j)

    def valid_move(self):
        if 'X' in board.rooms[self.loc_i][self.loc_j]:
            self.loc_i = self.current_loc[0]
            self.loc_j = self.current_loc[1]
            return False
        else:
            self.current_loc = [self.loc_i, self.loc_j]
            return True

class Demon(Entity):
    def __init__(self, name):
        super().__init__('@', name)
        self.patience = 3

    def move(self):
        move = board.random_loc()
        self.loc_i = move['i']
        self.loc_j = move['j']
        self.current_loc = [self.loc_i, self.loc_j]
    
    def greeting(self):
        print('Foolish mortal! Retrieve your weapon if you wish to face me...')
    


    

class Item(Entity):
    def init(self, name):
        super().__init__(name)


board = Board(5,5)
board.labrynth()
print(board.entities)
chara = Player(str(input("what's your name?..\n")))
demon = Demon('Pazuzu')
sword = Item('t', 'sword')
print(board.entities)
print(chara.current_loc, demon.current_loc)
board.print()

while True:
    chara.move(input(f'make a move, {chara.name}...'))
    print(chara.current_loc, demon.current_loc)
    if chara.current_loc == sword.current_loc:
        chara.inventory.append(sword)
    if chara.current_loc == demon.current_loc:
        if sword in chara.inventory:
            print('youwin')
            exit()
        else:
            demon.greeting()
    board.print()

    
                

