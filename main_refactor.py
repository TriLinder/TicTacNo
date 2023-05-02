# Define the board as a list of lists
# board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# Function to print the board
def print_board(board):
    print('\n'.join([' '.join(row) for row in board]))

# Function to check if the game is over
def is_game_over(board):
    # Check for a winner
    for i in range(3):
        if board[i][0] != '-' and board[i][0] == board[i][1] == board[i][2]:
            return True
        if board[0][i] != '-' and board[0][i] == board[1][i] == board[2][i]:
            return True
    if board[0][0] != '-' and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != '-' and board[0][2] == board[1][1] == board[2][0]:
        return True

    # Check for a tie
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True

# Function to get the next move from the player
def get_move(player):
    while True:
        move = int(input("Choose your move: "))
        row, col = move//3, move%3
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move.")
        elif board[row][col] != '-':
            print("Invalid move.")
        else:
            return row, col

# Play the game
print_board(board)
player = 'X'
while not is_game_over(board):
    row, col = get_move(player)
    board[row][col] = player
    print_board(board)
    if is_game_over(board):
        print("Player " + player + " wins!")
    elif player == 'X':
        player = 'O'
    else:
        player = 'X'
print("Game over.")
