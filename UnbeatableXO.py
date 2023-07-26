import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i + 1] + "|" + board[i + 2])
    print("-----")

# Function to check if the game is over (win, draw, or ongoing)
def check_game_over(board):
    # Define winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]

    # Check for a win
    for comb in winning_combinations:
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != "_":
            return board[comb[0]]  # Return the winning player ("X" or "O")

    # Check for a draw or incomplete game
    if "_" not in board:
        return "draw"  # Game is a draw
    else:
        return None  # Game is still ongoing

# Function to get the available moves on the board
def get_available_moves(board):
    return [i for i in range(9) if board[i] == "_"]

# Function to simulate a move on the board
def make_move(board, move, player):
    board[move] = player

# Function to undo a move on the board
def undo_move(board, move):
    board[move] = "_"

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    result = check_game_over(board)
    if result is not None:
        if result == "X":
            return -10 + depth  # Score if player (X) wins
        elif result == "O":
            return 10 - depth   # Score if AI (O) wins
        else:
            return 0  # Score if it's a draw

    if maximizing_player:
        max_eval = float("-inf")
        for move in get_available_moves(board):
            make_move(board, move, "O")
            eval = minimax(board, depth + 1, False, alpha, beta)
            undo_move(board, move)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in get_available_moves(board):
            make_move(board, move, "X")
            eval = minimax(board, depth + 1, True, alpha, beta)
            undo_move(board, move)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to get the best move for the computer using Minimax
def get_best_move(board):
    best_score = float("-inf")
    best_move = None
    for move in get_available_moves(board):
        make_move(board, move, "O")
        score = minimax(board, 0, False, float("-inf"), float("inf"))
        undo_move(board, move)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Function to play the Tic Tac Toe game
def play_unbeatable_xo():
    # Initialize the game board
    board = ["_" for _ in range(9)]

    # Determine who plays first
    player_turn = random.choice(["X", "O"])

    while True:
        print_board(board)

        if player_turn == "X":
            while True:
                try:
                    move = int(input("Enter your move (0-8): "))
                    if move not in range(9) or board[move] != "_":
                        print("Invalid move. Try again.")
                    else:
                        board[move] = "X"
                        break
                except ValueError:
                    print("Invalid input. Try again.")
        else:
            # Computer's turn
            best_move = get_best_move(board)
            board[best_move] = "O"

        # Check if the game is over
        result = check_game_over(board)
        if result:
            print_board(board)
            if result == "draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

        # Switch turns
        player_turn = "X" if player_turn == "O" else "O"

if __name__ == "__main__":
    play_unbeatable_xo()
