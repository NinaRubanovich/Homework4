import time

# Initialize the game board and constants
EMPTY = '.'
ROWS, COLS = 5, 6
WINNING_LENGTH = 4
INF = float("inf")

# Define the heuristic function
def heuristic(board, player):
    def count_open3(player):
        # Count two-side open and one-side open 3-in-a-row for the player
        count_2side_open, count_1side_open = 0, 0
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == player:
                    # Check horizontally
                    if col <= COLS - WINNING_LENGTH:
                        if board[row][col:col+WINNING_LENGTH].count(player) == 3:
                            count_2side_open += 1
                        elif board[row][col:col+WINNING_LENGTH].count('.') == 1:
                            count_1side_open += 1

                    # Check vertically
                    if row <= ROWS - WINNING_LENGTH:
                        if all(board[r][col] == player for r in range(row, row+WINNING_LENGTH)):
                            count_2side_open += 1
                        elif all(board[r][col] == '.' for r in range(row, row+WINNING_LENGTH - 1)):
                            count_1side_open += 1

                    # Check diagonally (down-right)
                    if col <= COLS - WINNING_LENGTH and row <= ROWS - WINNING_LENGTH:
                        diag = [board[row+i][col+i] for i in range(WINNING_LENGTH)]
                        if diag.count(player) == 3:
                            count_2side_open += 1
                        elif diag.count('.') == 1:
                            count_1side_open += 1

                    # Check diagonally (down-left)
                    if col >= WINNING_LENGTH - 1 and row <= ROWS - WINNING_LENGTH:
                        diag = [board[row+i][col-i] for i in range(WINNING_LENGTH)]
                        if diag.count(player) == 3:
                            count_2side_open += 1
                        elif diag.count('.') == 1:
                            count_1side_open += 1

        return count_2side_open, count_1side_open

    my_2side_open, my_1side_open = count_open3(player)
    opp_2side_open, opp_1side_open = count_open3('X' if player == 'O' else 'O')

    return (
        200 * my_2side_open - 80 * opp_2side_open +
        150 * my_1side_open - 40 * opp_1side_open
    )

# Check if a player has won
def is_winner(board, player):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == player:
                # Check horizontally
                if col <= COLS - WINNING_LENGTH and board[row][col:col+WINNING_LENGTH].count(player) == WINNING_LENGTH:
                    return True
                # Check vertically
                if row <= ROWS - WINNING_LENGTH and all(board[r][col] == player for r in range(row, row+WINNING_LENGTH)):
                    return True
                # Check diagonally (down-right)
                if col <= COLS - WINNING_LENGTH and row <= ROWS - WINNING_LENGTH:
                    diag = [board[row+i][col+i] for i in range(WINNING_LENGTH)]
                    if diag.count(player) == WINNING_LENGTH:
                        return True
                # Check diagonally (down-left)
                if col >= WINNING_LENGTH - 1 and row <= ROWS - WINNING_LENGTH:
                    diag = [board[row+i][col-i] for i in range(WINNING_LENGTH)]
                    if diag.count(player) == WINNING_LENGTH:
                        return True
    return False

# Check if the game has ended
def is_terminal(board):
    if is_winner(board, 'X'):
        return 1000
    elif is_winner(board, 'O'):
        return -1000
    elif all(board[row][col] != EMPTY for row in range(ROWS) for col in range(COLS)):
        return 0
    return None

# Check if a move is valid for player X
def is_valid_move(board, row, col, player):
    # Check if the position is within the board boundaries
    if not (0 <= row < ROWS and 0 <= col < COLS):
        return False

    # Check if the cell is empty
    if board[row][col] != EMPTY:
        return False

    # Check if the cell is adjacent to an existing 'X' piece horizontally, vertically, or diagonally
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                return True

    return False

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player, player):
    nodes_generated = 1

    result = is_terminal(board)
    if result is not None:
        return result, nodes_generated, None

    if depth == 0:
        return heuristic(board, player), nodes_generated, None

    if maximizing_player:
        max_eval = -INF
        best_move = None

        for col in range(COLS):
            for row in range(ROWS):
                if is_valid_move(board, row, col, player):
                    board[row][col] = player
                    eval, child_nodes_generated, _ = minimax(board, depth - 1, alpha, beta, False, player)
                    nodes_generated += child_nodes_generated
                    board[row][col] = EMPTY

                    if eval > max_eval:
                        max_eval = eval
                        best_move = (row, col)

                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break

        return max_eval, nodes_generated, best_move
    else:
        min_eval = INF
        best_move = None

        for col in range(COLS):
            for row in range(ROWS - 1, -1, -1):
                if board[row][col] == EMPTY:
                    board[row][col] = 'X' if player == 'O' else 'O'
                    eval, child_nodes_generated, _ = minimax(board, depth - 1, alpha, beta, True, player)
                    nodes_generated += child_nodes_generated
                    board[row][col] = EMPTY

                    if eval < min_eval:
                        min_eval = eval
                        best_move = (row, col)

                    beta = min(beta, eval)
                    if beta <= alpha:
                        break

        return min_eval, nodes_generated, best_move

# Print the board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Main game loop
def play_game():
    board = [[EMPTY] * COLS for _ in range(ROWS)]
    board[2][3] = 'X'
    board[2][2] = 'O'
    player = 'X'
    print_board(board)

    while True:
        if player == 'X':
            # Player X's turn
            start_time = time.time()
            _, nodes_generated, best_move = minimax(board, 2, -INF, INF, True, player)
            end_time = time.time()
            print(f"Player X generated {nodes_generated} nodes in {end_time - start_time:.5f} seconds")
            if best_move:
                row, col = best_move
                board[row][col] = player
        else:
            # Player O's turn
            start_time = time.time()
            _, nodes_generated, best_move = minimax(board, 4, -INF, INF, True, player)
            end_time = time.time()
            print(f"Player O generated {nodes_generated} nodes in {end_time - start_time:.5f} seconds")
            if best_move:
                row, col = best_move
                board[row][col] = player

        print_board(board)

        result = is_terminal(board)
        if result is not None:
            if result == 1000:
                print("Player X wins!")
            elif result == -1000:
                print("Player O wins!")
            else:
                print("It's a tie!")
            break

        player = 'X' if player == 'O' else 'O'

play_game()

### GAME ###
# Game start
# . . . . . .
# . . . . . .
# . . O X . .
# . . . . . .
# . . . . . .

# Player X generated 81 nodes in 0.00115 seconds
# . . . . . .
# . . X . . .
# . . O X . .
# . . . . . .
# . . . . . .

# Player O generated 5588 nodes in 0.11454 seconds
# . . . . . .
# . . X . . .
# . O O X . .
# . . . . . .
# . . . . . .

# Player X generated 94 nodes in 0.00166 seconds
# . X . . . .
# . . X . . .
# . O O X . .
# . . . . . .
# . . . . . .

# Player O generated 8546 nodes in 0.20444 seconds
# . X . . . .
# O . X . . .
# . O O X . .
# . . . . . .
# . . . . . .

# Player X generated 106 nodes in 0.00264 seconds
# . X . . . .
# O . X . . .
# . O O X . .
# . . . . X .
# . . . . . .

# Player X wins!