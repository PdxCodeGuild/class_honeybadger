class Player:
    def __init__(self,name,token):
        self.name = name
        self.token = token


class Game:
    def __init__(self,board):
        self.board = create_board

    def create_board(self,board):
        rows , columns = (3,3)
        array = [[0]*rows]*columns
        for row in array:
            print(row)
        return array



    def move(self,x,y,player):
        board.append([self.token])


    def calc_winner():
        pass

    def is_full():
        pass

    def is_game_over():
        pass

player1 = Player('bruce','x')
print(f'{player1.name} {player1.token}')

my_game = Game('board')
my_game.create_board(board)
board.move(1,2, player1)
