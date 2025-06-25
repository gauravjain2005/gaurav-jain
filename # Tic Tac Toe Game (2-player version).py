# Tic Tac Toe Game (2-player version)

def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_win(board, player):
    # All possible win combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_tie(board):
    return all(space in ['X', 'O'] for space in board)

def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number from 1 to 9.")
            elif board[move - 1] in ['X', 'O']:
                print("That spot is already taken. Choose another.")
            else:
                return move - 1
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    board = ['1','2','3','4','5','6','7','8','9']
    current_player = 'X'
    print("=== Welcome to Tic Tac Toe ===")
    print_board(board)

    while True:
        move = get_move(current_player, board)
        board[move] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif check_tie(board):
            print("🤝 It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
