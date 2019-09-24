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
        
    def labrynth(self):
        labrynth = []
        passages = self.width + (self.width + 1)
        corridors = self.height + (self.height + 1)
        
        for i in range(corridors):
            if i % 2 == 0:
                labrynth.append([['X'] for i in range(passages)])
            else:
                passage = []
                for j in range(passages):
                    if j % 2 == 0:
                        passage.append(['X'])
                    else:
                        passage.append(self.rooms[(i-1)//2][(j-1)//2])
                labrynth.append(passage)

        

        self.height = corridors
        self.width = passages
        self.rooms = labrynth
        # for i in range(len(self.rooms)):
        #     print(self.rooms[i], '\n')




    def print(self, entities):
        printable = ''
        
        for i in range(self.height): # sets entities
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].character in self.rooms[i][j] and (entities[k].loc_i != i or entities[k].loc_j != j):
                        self.rooms[i][j].remove(entities[k].character)
                    if entities[k].loc_i == i and entities[k].loc_j == j and entities[k].character not in self.rooms[i][j]:
                        self.rooms[i][j].append(entities[k].character)
                    
                        
        
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
        

class Player(Entity):
    def __init__(self, name):
        super().__init__('$', name)

    def move(self, command):
        if command == 'done':
            pass
        elif command in ['l', 'left', 'w', 'west']:
            self.loc_j -= 1  # move left
        elif command in ['r', 'right', 'e', 'east']:
            self.loc_j += 1  # move right
        elif command in ['u', 'up', 'n', 'north']:
            self.loc_i -= 1  # move up
        elif command in ['d', 'down', 's', 'south']:
            self.loc_i += 1 # move down
        if not self.valid_move():
            print('you ran into a wall...')
        
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
    
    def move(self):
        move = board.random_loc()
        self.loc_i = move['i']
        self.loc_j = move['j']
        self.current_loc = [self.loc_i, self.loc_j]
    
    def greeting(self):
        print('Foolish mortal!')
        exit()
    


        

board = Board(3, 3)
board.labrynth()
print(board.height, board.width)
m = board.random_loc()
print(m)
chara = Player(str(input("what's your name?..\n")))
demon = Demon('Pazuzu')
entities = [chara, demon]
print(chara.current_loc, demon.current_loc)
board.print(entities)

while True:
    chara.move(input(f'make a move, {chara.name}...'))
    print(chara.current_loc, demon.current_loc)
    if chara.current_loc == demon.current_loc:
        demon.greeting()
    board.print(entities)

    
                

