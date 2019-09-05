# creates player class with identification and token

class Player:
    def __init__(self, name, token):
        self.name = name
        self.toke = token

    def __eq__(self, other):
        if type(other) is Player:
            return self.token == other.token
#creates game class and iteration to make the board
class Game:
    def __init__(self):
        self.game = [[' ' for i in range(3)] for j in range(3)]

# board representation
    def __repr__(self):
        ret = ''
        for row in self.game:
            ret += '|'.join(row)
            ret += '\n'
        return ret
# if space has char in it, alert user; if space empty, place token.
    def place_token(self, x, y, token):
        if self.game[y][x] != ' ':
            return "Invalid move' Space taken."
        else:
            self.game[y][x] = token

# calculates winner by checking vertical, horisontal and diagonal wins
    def calc_winner(self):
        for i in range(3):
        row = self.game[i]
        if all(item == row[0]) and item != ' ' for item in row):
            return row [0]

        col = [self.game[j][i] for j in range (3)]
        if all (item == col[0] and item != ' ' for item in col):
            return col[0]

        if (self.game[0][0] == self.game[1][1] ==self.game[2][2]) and self.game[0][0] != ' ':
            return self.board[0][0]

        if (self.game[2][0] == self.game[1][1] ==self.game[0][2]) and self.game[2][0] != ' ':
            return self.game[2][0]

    def is_full(self):
        for row in self.game:
            if any (item ==' ' for item in row):
                return False
            return True
