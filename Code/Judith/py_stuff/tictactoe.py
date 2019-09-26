#filename: tictactoe.py

#############################################################

#classes

class Player:
    def __init__(self, name, tokens): #defines player objects as having names and token characters
        self.tokens = tokens
        self.name = name
    
    def __str__(self): #sets string form of player object as name
        return f'{self.name}'

class Game:
    def __init__(self): #initializer, defines board as nested list
        self.board = [['_' for i in range(3)] for i in range(3)]
    
    def __repr__(self): #sets board to print in more legible fashion
        return f'{self.board[0]}\n{self.board[1]}\n{self.board[2]}'
            

    def move(self, x, y, player):   #checks given space for token, places token and returns true if empty
        if self.board[x][y] == '_':
            self.board[x][y] = player.tokens
            return True
        else:
            print('cheater')
        
    
    def calc_winner(self):  #win conditions
        #starting position excluded from win conditions
        if self.board[0] == self.board[1] == self.board[2]:
            return 'start'
        #horizontal wins
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != '_':
            return 'win'
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != '_':
            return 'win'
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != '_':
            return 'win'
        #vertical wins
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != '_':
            return 'win' 
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != '_':
            return 'win' 
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != '_':
            return 'win'
        #diagonal wins
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '_':
            return 'win' 
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '_':
            return 'win'
        #no win condition met
        else:
            return 'pass turn'
 
    
    def isfull(self):   #returns True if board is full
        for l in self.board:
            if '_' in l:
                return False
        return True

    def isgameover(self):   #returns True if board is full or win condition has been met
        if self.isfull() == True or self.calc_winner() == 'win':
            return True
        else:
            return False
        
        

#############################################################

def main():
    
    playerOne = Player(input('name: '), 'X')
    playerTwo = Player(input('name: '), 'O')
    players = [playerOne, playerTwo]

    newgame = Game()
    # print(newgame.__repr__())
    # print(newgame.isfull())
    # print(newgame.calc_winner())
    # print(newgame.isgameover())

    while newgame.isgameover() == False:
        for player in players:
            if newgame.isgameover() == False:
                print(player,' turn')
                m_flag = False          #flag and internal while loop set up to repeat turn in case of invalid move
                while m_flag == False:    
                     if newgame.move(int(input('row: ')),int(input('col: ')),player):
                         m_flag = True
                print(newgame.__repr__())
                print(newgame.calc_winner())
                if newgame.calc_winner() == 'win':
                    print(player,' is the winner!')
                elif newgame.isfull() == True:
                    print('draw...')
        
        
        
main()       
