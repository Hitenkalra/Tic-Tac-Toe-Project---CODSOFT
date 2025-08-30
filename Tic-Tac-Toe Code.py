import math

# Tic-Tac-Toe AI (Human vs AI) using Minimax Algorithm
# Human plays 'O', AI plays 'X'

def print_board(board):
    """Display the board in a user-friendly way."""
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n")


def is_winner(board, player):
    """Check if a player has won."""
    # Rows, Columns, Diagonals
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_states


def is_full(board):
    """Check if the board is full (tie)."""
    for row in board:
        if " " in row:
            return False
    return True


def minimax(board, depth, is_maximizing):
    """Minimax algorithm to find best move."""
    if is_winner(board, "X"):
        return 1
    if is_winner(board, "O"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


def best_move(board):
    """Find the best move for AI."""
    move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def play_game():
    """Main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'O', AI is 'X'.")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0,1,2): "))
                col = int(input("Enter col (0,1,2): "))
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break
                else:
                    print("That spot is taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid input, please enter 0, 1 or 2.")

        print_board(board)

        if is_winner(board, "O"):
            print("🎉 You win! Congratulations!")
            break
        if is_full(board):
            print("It's a Tie!")
            break

        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "X"
        print("AI chose:", ai_row, ai_col)
        print_board(board)

        if is_winner(board, "X"):
            print("😎 AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a Tie!")
            break


# Run the game
if __name__ == "__main__":
    play_game()
