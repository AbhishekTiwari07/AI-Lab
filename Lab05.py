import numpy as np

class Board:
    def __init__(self, board=None, maxplayer=True):
        self.win = 0
        self.lost = 0
        self.total_games = 0
        self.nodes = 0
        self.alpha = -1000000
        self.beta = 1000000
        self.maximizingPlayer = maxplayer
        self.board = [['_' for j in range(3)] for i in range(3)]

        if board is not None:
            self.board = board

    def print_board(self):
        for x in self.board:
            print(x)
        print()

    def changePlayer(self):
        self.maximizingPlayer = not self.maximizingPlayer

    def evaluation(self):
        board = self.board

        #check rows
        for i in range(3):
            if board[i][0] != '_' and (board[i][0] == board[i][1] and board[i][1] == board[i][2]):
                return 10 if self.maximizingPlayer else -10 

        #check cols
        for i in range(3):
            if board[0][i] != '_' and (board[0][i] == board[1][i] and board[1][i] == board[2][i]):
                return 10 if self.maximizingPlayer else -10
        
        #check diagonals
        if board[0][0] != '_' and  board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return 10 if self.maximizingPlayer else -10

        if board[2][0] != '_' and  board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            return 10 if self.maximizingPlayer else -10

        return 0

    def isMovesLeft(self):
        board = self.board
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_' :
                    return True
        return False  

    def minimax(self, depth, maxPlayer):
        self.nodes += 1
        self.maximizingPlayer = maxPlayer
        board = self.board
        score = self.evaluation()
        purana_value = None
        naya_value = None
        
        if score == 10:
            self.win += 1
            return score

        if score == -10:
            self.lost += 1
            return score

        if not self.isMovesLeft():
            self.total_games += 1
            return 0


        bestConfig = self.board

        if maxPlayer:
            purana_value = -100000

            for i in range(3):
                for j in range(3): 
                    # Best move for max player
                    if board[i][j] == '_':
                        board[i][j] = 'x'
                        naya_value = max(purana_value, self.minimax(depth + 1, False))
                        if purana_value < naya_value:
                            bestConfig = board
                            purana_value = naya_value

                        board[i][j] = '_'
        
        else:
            purana_value = 100000

            for i in range(3):
                for j in range(3): 
                    # Best move for min player
                    if board[i][j] == '_':
                        board[i][j] = 'o'
                        naya_value = min(purana_value, self.minimax(depth + 1, True))
                        if purana_value > naya_value:
                            bestConfig = board
                            purana_value = naya_value

                        board[i][j] = '_'


        self.board = bestConfig

        return naya_value - depth

    def alphabeta(self, depth, maxPlayer):
        self.nodes += 1
        self.maximizingPlayer = maxPlayer
        # print(self.maximizingPlayer)
        board = self.board
        score = self.evaluation()
        purana_value = None
        naya_value = None
        
        if score == 10:
            self.lost += 1
            return score
            
        if score == -10:
            self.win += 1
            return score

        if not self.isMovesLeft():
            self.total_games += 1
            return 0


        bestConfig = self.board

        flag = False

        if maxPlayer:
            purana_value = -100000

            for i in range(3):
                for j in range(3): 
                    # Best move for max player
                    if board[i][j] == '_':
                        board[i][j] = 'x'
                        naya_value = max(purana_value, self.alphabeta(depth + 1, False))

                        self.alpha = max(self.alpha, naya_value)
                        # print("A", self.alpha, self.beta)

                        if self.beta <= self.alpha:
                            board[i][j] = '_'
                            flag = True
                            break

                        if purana_value < naya_value:
                            bestConfig = board
                            purana_value = naya_value

                        board[i][j] = '_'
                # if flag:
                #     break
        
        else:
            purana_value = 100000

            for i in range(3):
                for j in range(3): 
                    # Best move for min player
                    if board[i][j] == '_':
                        board[i][j] = 'o'
                        naya_value = min(purana_value, self.alphabeta(depth + 1, True))

                        self.beta = min(self.beta, naya_value)

                        if self.beta >= self.alpha:
                            board[i][j] = '_'
                            flag = True
                            break

                        if purana_value > naya_value:
                            bestConfig = board
                            purana_value = naya_value

                        board[i][j] = '_'

                # if flag:
                #     break

        self.board = bestConfig

        return naya_value - depth
 

# board = Board([['x', '_', '_'], ['_', 'o', '_'], ['_', 'x', '_']])
# board = Board()
board = Board([['_', 'o', 'o'], ['x', 'x', '_'], ['x', '_', '_']])
# board = Board([['x', 'o', '_'], ['x', '_', 'o'], ['o', 'x', '_']])
# board = Board([['x', '_', 'o'], ['_', 'x', '_'], ['_', '_', '_']])

board.print_board()

# board.alphabeta(0, False)

board.minimax(0, False)

print('Win ',board.win)
print('Lost ',board.lost)
print('Draw ', board.total_games)
print('Total Games', board.total_games+board.win+board.lost)
print('Total Nodes ', board.nodes)
# if board.total_games+board.win+board.lost == 255168:
#     print("MINIMAX Badiya Chal rha")