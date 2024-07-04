import numpy as np

# Constants for the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Define the Tic-Tac-Toe board
class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), EMPTY)  # 3x3 board filled with empty spaces
        self.current_player = PLAYER_X       # Player X starts first

    def print_board(self):
        print("-------------")
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("-------------")

    def is_empty(self, row, col):
        return self.board[row][col] == EMPTY

    def make_move(self, row, col):
        if self.is_empty(row, col):
            self.board[row][col] = self.current_player
            self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
            return True
        return False

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != EMPTY:
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != EMPTY:
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return self.board[0][2]

        # Check for a draw
        if np.all(self.board != EMPTY):
            return 'DRAW'

        # No winner yet
        return None

    def is_game_over(self):
        return self.check_winner() is not None

    def get_empty_positions(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == EMPTY]

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = board.check_winner()

    if winner == PLAYER_X:
        return -1  # Player X wins
    elif winner == PLAYER_O:
        return 1   # Player O wins
    elif winner == 'DRAW':
        return 0   # It's a draw

    if is_maximizing:
        max_eval = -np.inf
        for row, col in board.get_empty_positions():
            board.board[row][col] = PLAYER_O
            eval = minimax(board, depth + 1, False, alpha, beta)
            board.board[row][col] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = np.inf
        for row, col in board.get_empty_positions():
            board.board[row][col] = PLAYER_X
            eval = minimax(board, depth + 1, True, alpha, beta)
            board.board[row][col] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board):
    best_eval = -np.inf
    best_move = None
    alpha = -np.inf
    beta = np.inf

    for row, col in board.get_empty_positions():
        board.board[row][col] = PLAYER_O
        eval = minimax(board, 0, False, alpha, beta)
        board.board[row][col] = EMPTY

        if eval > best_eval:
            best_eval = eval
            best_move = (row, col)

    return best_move

def play_game():
    game = TicTacToe()
    game.print_board()

    while not game.is_game_over():
        if game.current_player == PLAYER_X:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if game.make_move(row, col):
                game.print_board()
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is making a move...")
            row, col = find_best_move(game)
            game.make_move(row, col)
            game.print_board()

    winner = game.check_winner()
    if winner == 'DRAW':
        print("It's a draw!")
    else:
        if winner == PLAYER_X:
            print("You win!")
        else:
            print("AI wins!")

# Start the game
play_game()

