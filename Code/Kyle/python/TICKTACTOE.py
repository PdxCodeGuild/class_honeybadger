# class player:
#     def __init__(self, name, team):
#         self.name = name
#         self.team = team

class game:
    def __init__(self, board):
        self.board = board

def build_board():
    rows, cols = (3, 3)
    structure = [[0]*cols]*rows
    for rows in structure:
        print(rows)
    return structure

build_board()


