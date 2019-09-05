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

    def pretty_board(self):
        row_1 = self.board[:3]
        row_2 = self.board[3:6]
        row_3 = self.board[6:]
        print(f"{row_1[0]} | {row_1[1]} | {row_1[2]}")
        print(f"{row_2[0]} | {row_2[1]} | {row_2[2]}")
        print(f"{row_3[0]} | {row_3[1]} | {row_3[2]}")

# This calculates the winner. Really long code. I could probably make this much more concise.

    def calc_winner(self):
        win_player_1 = [" X", " X", " X"]
        win_player_2 = [" O", " O", " O"]
        winner = False
        while winner is False:
            # Playr 1:
            # 1 - horizontal, first row across
            if self.board[0:3] == win_player_1[0:3]:
                print("\nPlayer 1 wins!")
                winner = True
            # 2 - horizontal, second row across
            elif self.board[3:6] == win_player_1[0:3]:
                print("\nPlayer 1 wins!")
                winner = True
            # 3 - horizontal, third row across
            elif self.board[6:9] == win_player_1[0:3]:
                print("\nPlayer 1 wins!")
                winner = True
            # 4 - diagonal, top-left to bottom-right
            elif self.board[0] == win_player_1[0] and self.board[4] == win_player_1[1] and self.board[8] == win_player_1[2]:
                print("\nPlayer 1 wins!")
                winner = True
            # 5 - diagonal, top-right to bottom-left
            elif self.board[2] == win_player_1[0] and self.board[4] == win_player_1[1] and self.board[6] == win_player_1[2]:
                print("\nPlayer 1 wins!")
                winner = True
            # 6 - vertical, left
            elif self.board[0] == win_player_1[0] and self.board[3] == win_player_1[1] and self.board[6] == win_player_1[2]:
                print("\nPlayer 1 wins!")
                winner = True
            # 7 - vertical, middle
            elif self.board[1] == win_player_1[0] and self.board[4] == win_player_1[1] and self.board[7] == win_player_1[2]:
                print("\nPlayer 1 wins!")
                winner = True
            # 8 - vertical, right
            elif self.board[2] == win_player_1[0] and self.board[5] == win_player_1[1] and self.board[8] == win_player_1[2]:
                print("\nPlayer 1 wins!")
                winner = True
            
            # Player 2:
            # 1 - horizontal, first row across
            elif self.board[0:3] == win_player_2[0:3]:
                print("\nPlayer 2 wins!")
                winner = True
            # 2 - horizontal, second row across
            elif self.board[3:6] == win_player_2[0:3]:
                print("\nPlayer 2 wins!")
                winner = True
            # 3 - horizontal, third row across
            elif self.board[6:9] == win_player_2[0:3]:
                print("\nPlayer 2 wins!")
                winner = True
            # 4 - diagonal, top-left to bottom-right
            elif self.board[0] == win_player_2[0] and self.board[4] == win_player_2[1] and self.board[8] == win_player_2 [2]:
                print("\nPlayer 2 wins!")
                winner = True
            # 5 - diagonal, top-right to bottom-left
            elif self.board[2] == win_player_2[0] and self.board[4] == win_player_2[1] and self.board[6] == win_player_2[2]:
                print("\nPlayer 2 wins!")
                winner = True
            # 6 - vertical, left
            elif self.board[0] == win_player_2[0] and self.board[3] == win_player_2[1] and self.board[6] == win_player_2[2]:
                print("\nPlayer 2 wins!")
                winner = True
            # 7 - vertical, middle
            elif self.board[1] == win_player_2[0] and self.board[4] == win_player_2[1] and self.board[7] == win_player_2[2]:
                print("\nPlayer 2 wins!")
                winner = True
            # 8 - vertical, right
            elif self.board[2] == win_player_2[0] and self.board[5] == win_player_2[1] and self.board[8] == win_player_1[2]:
                print("\nPlayer 2 wins!")
                winner = True
            else:
                break
        return winner

# This determines if the board is full or not. The is_full() will return "True" if the board is full. By default it is set to "False".

    def is_full(self):
        plays = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        is_it_full = False
        for play in plays:
            if play in self.board:
                break
        else:
            is_it_full = True
        return is_it_full

# This determines if the game is over. By default it is set to "False".

    def game_over(self):
        end_game = False
        if self.calc_winner() is True:
            end_game = True
        elif self.is_full() is True:
            end_game = True
            print("\nThe board is full.")
        return end_game

# This is the main game that runs everything

def main():
    game = Game()
    player_1 = input("\nPlayer 1, please enter your name: ")
    player_1_play = Player(player_1, " X")
    print(f"\n{player_1}, your token is: {player_1_play.token}")
    player_2 = input("\nPlayer 2, please enter your name: ")
    player_2_play = Player(player_2, " O")
    print(f"\n{player_2}, your token is: {player_2_play.token}")
    game.board = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    game_board = game.board
    # print(game_board)
    print("\nHere is your board:\n")
    game.pretty_board()
    round_count = 1
    while game.game_over() is False:
            # player turn:
        if round_count % 2 == 1:
            player = player_1
            token = player_1_play.token
        elif round_count %2 == 0:
            player = player_2
            token = player_2_play.token
        print(f"\n\nRound #{round_count}\n")
        round_count += 1
        round = input(f"{player}, please choose a position: ")
        for index, x in enumerate(game_board):
            if x == round:
                game_board[index] = token
                game.game_over()
                print("\n")
                game.pretty_board()
    else:
        print("\nGame over.\n")


print(main())

# Still needs:
# - user validation (use try/except)
# - change board to be empty using a dictionary (not a1, a2, etc.)
# - remove "None" from end
# - Loop to play a new game