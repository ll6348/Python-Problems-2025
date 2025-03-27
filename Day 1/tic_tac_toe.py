import random

def tic_tac_toe(user_symbol, computer_symbol):
    """
    Play a Tic-Tac-Toe game between the computer (Player 1) and the user (Player 2).
    
    - Player 1 (Computer) selects the best available move.
    - Player 2 (User) inputs row and column to mark 'X' or 'O'.
    - The game continues until a player wins or all cells are occupied (draw).
    - The board is printed after each move.
    """
    list_for_choices = [[i, j] for i in range(3) for j in range(3)]
    game_board = [[' ' for _ in range(3)] for _ in range(3)]
    
    while True:
        for row in game_board:
            print(row)

        try:
            user_choice = list(map(int, input("Choose a position (row,col): ").split(',')))
            if user_choice not in list_for_choices:
                print("Invalid choice! Choose an empty position.")
                continue
        except ValueError:
            print("Invalid input format! Enter row and column separated by a comma (e.g., 0,1).")
            continue

        game_board[user_choice[0]][user_choice[1]] = user_symbol
        list_for_choices.remove(user_choice)

        if check_winner(game_board, user_symbol):
            for row in game_board:
                print(row)
            print("User won!")
            break

        if not list_for_choices:
            for row in game_board:
                print(row)
            print("It's a Draw!")
            break

        computer_choice = find_best_move(game_board, list_for_choices, user_symbol, computer_symbol)
        game_board[computer_choice[0]][computer_choice[1]] = computer_symbol
        list_for_choices.remove(computer_choice)

        if check_winner(game_board, computer_symbol):
            for row in game_board:
                print(row)
            print("Computer won!")
            break

def check_winner(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False

def find_best_move(board, choices, user_symbol, computer_symbol):
    for move in choices:
        temp_board = [row[:] for row in board]
        temp_board[move[0]][move[1]] = computer_symbol
        if check_winner(temp_board, computer_symbol):
            return move

    for move in choices:
        temp_board = [row[:] for row in board]
        temp_board[move[0]][move[1]] = user_symbol
        if check_winner(temp_board, user_symbol):
            return move

    if [1,1] in choices:
        return [1,1]

    for corner in [[0,0], [0,2], [2,0], [2,2]]:
        if corner in choices:
            return corner

    return random.choice(choices)

user_choice = input("Choose 'X' or 'O': ").upper()
while user_choice not in ['X', 'O']:
    user_choice = input("Invalid choice! Choose 'X' or 'O': ").upper()

computer_choice = 'O' if user_choice == 'X' else 'X'
tic_tac_toe(user_choice, computer_choice)
