# tic_tac_toe_v2.py

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        pass

    def board(self, board):
        self.board = board
        game_board = board
        return game_board
        
    def move(self, x, y, player):
        pass
    
    def __str__(self):
        pass

# This makes the board pretty. It uses indexing to turn one list into three lists.
# Stil a WIP. I need to turn the lists display without brackets and quotes.

    def pretty_board(self):
        row_1 = self.board[:3]
        row_2 = self.board[3:6]
        row_3 = self.board[6:]
        print(row_1)
        print(row_2)
        print(row_3)        

# This calculates the winner. Still WIP.

    def calc_winner(self):
        win_player_1 = ["X", "X", "X"]
        win_player_2 = ["O", "O", "O"]
        winner = False
        while winner is False:
            if self.board[0:3] == win_player_1[0:3]:
                print("Player 1 wins!")
                winner = True
            elif self.board[0:3] == win_player_2[0:3]:
                print("Player 2 wins!")
                winner = True
            else:
                break
        return winner

# This determins if the board is full or not. The is_full() will return "True" if the board is full. By default it is set to "False".

    def is_full(self):
        plays = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        # print(plays)
        # print(f"{self.board}")
        is_it_full = False
        for play in plays:
            if play in self.board:
                break
        else:
            is_it_full = True
        return is_it_full
    
    def game_over(self):
        end_game = False
        self.calc_winner()
        self.is_full()
        if self.calc_winner() is True:
            end_game = True
        elif self.is_full() is True:
            end_game = True
        return end_game

# This is the main game that runs everything

def main():
    game = Game()
    player_1 = input("Player 1, please enter your name: ")
    player_1_play = Player(player_1, "X")
    print(f"{player_1}, your token is: {player_1_play.token}\n")
    player_2 = input("Player 2, please enter your name: ")
    player_2_play = Player(player_2, "O")
    print(f"{player_2}, your token is: {player_2_play.token}\n")
    game.board = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    game_board = game.board
    # print(game_board)
    print("Here is your board:\n")
    game.pretty_board()
    while game.game_over() is False:
        while game.calc_winner() is False:
            while game.is_full() is False:
            # player 1's turn
                round_a = input(f"{player_1}, please choose a position: ")
                for index, x in enumerate(game_board):
                    if x == round_a:
                        game_board[index] = player_1_play.token
                        game.game_over()
                print("\n")
                game.pretty_board()
                    
                # player 2's turn
                
                round_b = input(f"{player_2}, please choose a position: ")
                for index, x in enumerate(game_board):
                    if x == round_b:
                        game_board[index] = player_2_play.token
                        game.game_over()
                print(f"Is the game full? -- {game.is_full()}")
                print("\n")
                game.pretty_board()
        else:
            print("Game over.")
            break
    else:
        print("Game over.")


print(main())
# print(main())
# test = Game("a3")
# print(f"{test.board}")