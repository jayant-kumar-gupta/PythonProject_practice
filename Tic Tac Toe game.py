import random

def print_board(board):
    print("------------------------------------------")
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    for row in board:
        if any([spot == " " for spot in row]):
            return False
    return True

def player_move(board, player):
    while True:
        try:
            move = input("Enter your move (row and column) separated by a space: ").split()
            if len(move) != 2:
                raise ValueError("Invalid input. Please enter two numbers separated by a space.")
            row, col = int(move[0]), int(move[1])
            if row not in range(3) or col not in range(3):
                raise ValueError("Invalid move. Row and column must be between 0 and 2.")
            if board[row][col] != " ":
                raise ValueError("Invalid move. The spot is already taken.")
            board[row][col] = player
            break
        except ValueError as e:
            print(e)

def ai_move(board, player):
    opponent = "X"
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board, player):
                    return
                board[row][col] = " "
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = opponent
                if check_winner(board, opponent):
                    board[row][col] = player
                    return
                board[row][col] = " "
    empty_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    move = random.choice(empty_spots)
    board[move[0]][move[1]] = player

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0
    scores = {"Player": 0, "AI": 0}

    while True:
        print_board(board)
        current_player = players[current_player_index]

        if current_player == "X":
            player_move(board, current_player)
        else:
            ai_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            winner = "Player" if current_player == "X" else "AI"
            print("------------------------------------------")
            print(f"{winner} wins!")
            scores[winner] += 1
            print(f"Scores: Player {scores['Player']} - AI {scores['AI']}")
            print("------------------------------------------")
            if input("Play again? (yes/no): ").lower() != "yes":
                break
            board = [[" " for _ in range(3)] for _ in range(3)]
            continue

        if is_board_full(board):
            print_board(board)
            print("------------------------------------------")
            print("It's a tie!")
            print("------------------------------------------")
            if input("Play again? (yes/no): ").lower() != "yes":
                break
            board = [[" " for _ in range(3)] for _ in range(3)]
            continue

        current_player_index = (current_player_index + 1) % 2

if __name__ == "__main__":
    play_game()