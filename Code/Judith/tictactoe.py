#filename: tictactoe.py

#############################################################

#classes

class Player:
    def __init__(self, name, tokens):
        self.tokens = tokens
        self.name = name
    
    def __str__(self):
        return f'{self.name}'

class Game:
    def __init__(self):
        self.board = [['_' for i in range(3)] for i in range(3)]
    
    def __repr__(self):
        return f'{self.board}'

    def move(self, x, y, player):
        if self.board[x][y] == '_':
            self.board[x][y] = player.tokens  
        else:
            print('cheater')
        
    
    def calc_winner(self):
        if self.board[0] == self.board[1] == self.board[2]:
            return 'start'
        
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != '_':
            return 'win'
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != '_':
            return 'win'
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != '_':
            return 'win'

        elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != '_':
            return 'win' 
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != '_':
            return 'win' 
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != '_':
            return 'win'

        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '_':
            return 'win' 
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '_':
            return 'win'
        
        else:
            return 'pass turn'
 
    
    def isfull(self):
        for l in self.board:
            if '_' in l:
                return True
            else:
                return False

    def isgameover(self):
        if self.isfull() == False or self.calc_winner() == 'win':
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
                newgame.move(int(input('row: ')),int(input('col: ')),player)
                print(newgame.__repr__())
                print(newgame.calc_winner())
                if newgame.calc_winner() == 'win':
                    print(player,' is the winner!')
                elif newgame.isfull() == False:
                    print('draw...')
        
        
        
main()       
