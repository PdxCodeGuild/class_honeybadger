class game:
    def __init__(self):
        self.board = [['_' for i in range(3)] for i in range(3)]
    
    def __repr__(self):
        return f'{self.board}'

newgame = game()

print(newgame)