board = [" "] * 9

def display():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def check_win(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in wins
    )

player = "X"

while " " in board:
    display()
    position = int(input(f"Player {player}, enter position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid position!")
        continue

    board[position] = player

    if check_win(player):
        display()
        print("Player", player, "wins!")
        break

    player = "O" if player == "X" else "X"
else:
    display()
    print("It's a draw!")
