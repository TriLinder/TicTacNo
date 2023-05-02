def print_board(board):
    print('\n\nThis is the current board state:\n'+'\n'.join([' '.join(board[3*i:3*(i+1)]) for i in range(3)]))

def is_game_over(board):
    return True if any([(board[3*i] != '-' and board[3*i] == board[3*i + 1] == board[3*i + 2]) or (board[i] != '-' and board[i] == board[3+i] == board[6+i]) for i in range(3)]) or (board[0] != '-' and board[0] == board[4] == board[8]) or (board[2] != '-' and board[2] == board[4] == board[6]) else '-' not in board

def get_move(board):
    return (lambda f: lambda a: f(f, a))(lambda rec, move: [print('Invalid move.'), rec(rec, int(input("\nChoose your move: ")))][1] if (move < 0 or move > 8) or (board[move] != '-') else move)(int(input("\nChoose your move: ")))

def main(board):
    print_board(board)
    player = 'X'
    while not is_game_over(board):
        move = get_move(board)
        board[move] = player
        print_board(board)
        if is_game_over(board):
            # print("Player " + player + " wins!")
            pass
        elif player == 'X':
            player = 'O'
        else:
            player = 'X'
    print("Game over.")
    
main(['-', '-', '-', '-', '-', '-', '-', '-', '-'])