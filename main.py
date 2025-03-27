import os


def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")  # Clears the console for better visuals

    
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]

    return [player, player, player] in win_conditions

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter a position (1-9): ")) - 1
            row, col = move // 3, move % 3
            if 0 <= move < 9 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move! The spot is already taken or out of range.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def play_game():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        print_board(board)

        while True:
            row, col = get_player_move(board, current_player)
            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"🎉 Player {current_player} wins! 🎉")
                break
            elif is_draw(board):
                print("It's a draw! 🤝")
                break

            current_player = "O" if current_player == "X" else "X"  # Switch player
        
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    play_game()
