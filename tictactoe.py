def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That position is already taken. Try again.")
            continue

        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

    replay = input("Do you want to play again? (yes/no): ")
    if replay.lower() == "yes":
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
