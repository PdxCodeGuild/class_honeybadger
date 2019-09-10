# tic_tac_toe.py

class Player1:
    def __init__(self, name, token = " X"):
        self.name = name
        self.token = token

class Player2:
    def __init__(self, name, token = " O"):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        pass

    def board(self, board_1, board_2, board_3):
        self.board_1 = board_1
        self.board_2 = board_2
        self.board_3 = board_3
        game_board = [self.board_1, self.board_2, self.board_3]
        return game_board
        
    def move(self, x, y, player):
        pass
    
    def __str__(self):
        pass
        
    def calc_winner(self, board):
        # board = []
        pass
    
    def is_full(self):
        plays = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        play_check = self.board(self.board_1, self.board_2, self.board_3)
        # print(f"{play_check}")
        # if "a1" or "a2" or "a3" or "b1" or "b2" or "b3" or "c1" or "c2" or "c3" in play_check:
        #     return False
        # else:
        #     return True
        for row in play_check:
            for position in plays:
                if position in row:
                    return False
                
                

def main():
    game = Game()
    player_1 = input("Player 1, please enter your name: ")
    player_1_play = Player1(player_1)
    print(f"{player_1}, your token is: {player_1_play.token}\n")
    player_2 = input("Player 2, please enter your name: ")
    player_2_play = Player2(player_2)
    print(f"{player_2}, your token is: {player_2_play.token}\n")
    game.board_1 = ["a1", "|", "a2", "|", "a3"]
    game.board_2 = ["b1", "|", "b2", "|", "b3"]
    game.board_3 = ["c1", "|", "c2", "|", "c3"]
    board_play = game.board(game.board_1, game.board_2, game.board_3)
    game_over = False
    # print(f"{game.is_full}")
    # print(full)
    print("Here is your board:\n")
    for y in board_play:
        print(*y)
    while game_over is False:
        while game.is_full() is False:
            # player 1's turn
            round_a = input(f"\n{player_1}, please choose a position: ")
            for index, x in enumerate(game.board_1):
                if x == round_a:
                    game.board_1[index] = player_1_play.token
                    game.is_full()
            for index, x in enumerate(game.board_2):
                if x == round_a:
                    game.board_2[index] = player_1_play.token
                    game.is_full()
            for index, x in enumerate(game.board_3):
                if x == round_a:
                    game.board_3[index] = player_1_play.token
                    game.is_full()
            print(f"Is the game full? -- {game.is_full()}")
            print("\n")
            for y in board_play:
                print(*y)
                
            # player 2's turn
            round_b = input(f"\n{player_2}, please choose a position: ")
            for index, x in enumerate(game.board_1):
                if x == round_b:
                    game.board_1[index] = player_2_play.token
                    game.is_full()
            for index, x in enumerate(game.board_2):
                if x == round_b:
                    game.board_2[index] = player_2_play.token
                    game.is_full()
            for index, x in enumerate(game.board_3):
                if x == round_b:
                    game.board_3[index] = player_2_play.token
                    game.is_full()
            print(f"Is the game full? -- {game.is_full()}")
            print("\n")
            for y in board_play:
                print(*y)
        else:
            game_over == True
            print("Game over.")


print(main())
# print(main())
# test = Game("a3")
# print(f"{test.board}")