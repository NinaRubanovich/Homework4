# HOMEWORK 4
Group 6: Jade Neeley, Gavin Boley, Nina Rubanovich

## IMPLEMENTATIONS
This code is an implementation of a simple game called "Connect Four" within a grid of 5 rows and 6 columns. The game is played between two players, X and O, taking turns to make a move in an attempt to form a sequence of 4 of their pieces either horizontally, vertically, or diagonally. The game employs the minimax algorithm with alpha-beta pruning to make optimal moves, and it uses a heuristic function to evaluate the game state.

### Game Setup and Constants:

It initializes the game board, represented as a grid with rows and columns.
It defines the constants like 'EMPTY' (to represent an empty cell), 'WINNING_LENGTH' (the number of pieces required to win), and 'INF' (infinity) for use in the minimax algorithm.

### Heuristic Function (heuristic):

The heuristic function evaluates the desirability of a game state for a given player.
It checks for various patterns on the game board, including open three-in-a-row situations.
It assigns a score to each state based on the patterns, considering both offensive and defensive strategies.

### Winning and Terminal Conditions:

The 'is_winner' function checks if a player has won the game by forming a sequence of 'WINNING_LENGTH' pieces in any direction.
The 'is_terminal' function checks if the game has ended due to a win, loss, or a draw.

### Valid Move Validation (is_valid_move):

This function checks if a move (placing a piece) is valid for the current player.
It ensures that the move is within the board boundaries, the cell is empty, and it is adjacent to an existing piece (horizontally, vertically, or diagonally).

### Minimax Algorithm with Alpha-Beta Pruning (minimax):

The minimax algorithm is used to find the best move for a player.
It explores possible moves on the game board up to a certain depth and evaluates each resulting game state using the heuristic function.
Alpha-beta pruning is employed to minimize the number of evaluated game states and improve efficiency.
The function returns the best move and the associated score for the current player.

### Print Board (print_board):

This function is used to print the current state of the game board to the console.

### Main Game Loop (play_game):

The main game loop initializes the game board, starts with a given board configuration, and lets players ('X' and 'O') take turns.
It uses the minimax algorithm to determine the best moves for each player.
The game loop continues until a player wins or the game ends in a draw.

## GAME RESULS

### Game start
. . . . . .
. . . . . .
. . O X . .
. . . . . .
. . . . . .

### Player X generated 81 nodes in 0.00115 seconds
. . . . . .
. . X . . .
. . O X . .
. . . . . .
. . . . . .

### Player O generated 5588 nodes in 0.11454 seconds
. . . . . .
. . X . . .
. O O X . .
. . . . . .
. . . . . .

### Player X generated 94 nodes in 0.00166 seconds
. X . . . .
. . X . . .
. O O X . .
. . . . . .
. . . . . .

### Player O generated 8546 nodes in 0.20444 seconds
. X . . . .
O . X . . .
. O O X . .
. . . . . .
. . . . . .

### Player X generated 106 nodes in 0.00264 seconds
. X . . . .
O . X . . .
. O O X . .
. . . . X .
. . . . . .

### Player X wins!