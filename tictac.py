import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if any player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the board is full (tie condition)
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

# Find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main function for the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's turn
        row, col = map(int, input("Enter your move (row and column, 0-2): ").split())
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI's turn
        print("AI's turn...")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("AI wins! Better luck next time!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)

play_game()
