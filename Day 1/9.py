import random

def tic_tac_toe(user_number, computer_number):
    is_true_1 = True
    list_for_choices = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
    game_board = [[' ' for _ in range(3)] for _ in range(3)]
    while is_true_1:
        print(game_board)
        user_choice = tuple(map(int, input("Choose a position from the board: [[(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)]] ").split(' ')))

        if game_board[user_choice[0]][user_choice[1]] == " ":
            game_board[user_choice[0]][user_choice[1]] = user_number
            list_for_choices.remove(list(user_choice))
        else:
            print("Position already taken")
            continue

        bound = 2

        for i in range(3):
            for j in range(3):
                user_wins = False
                if i+2 <= bound and game_board[i][j] == game_board[i+1][j] == game_board [i+2][j] != ' ':
                    user_wins = True
                    if user_wins == True:
                        break
                if j+2 <= bound and game_board[i][j] == game_board[i][j+1] == game_board [i][j+2] != ' ':
                    user_wins = True
                    if user_wins == True:
                        break
                if i+2 <= bound and j+2 <= bound and game_board[i][j] == game_board[i+1][j+1] == game_board [i+2][j+2] != ' ':
                    user_wins = True
                    if user_wins == True:
                        break
                if i-1 >= 0 and j-1 >= 0 and i+1 <= 2 and j+1 <= 2 and game_board[i-1][j+1] == game_board[i][j] == game_board[i+1][j-1] != ' ':
                    user_wins = True
                    if user_wins == True:
                        break

        if user_wins == True:
            print("User won!")
            break

        is_true = True
        while is_true:
            computer_choice = list(random.choice(list_for_choices))

            if game_board[computer_choice[0]][computer_choice[1]] == " ":
                game_board[computer_choice[0]][computer_choice[1]] = computer_number
                list_for_choices.remove(list(computer_choice))
                is_true = False

        for i in range(3):
            for j in range(3):
                computer_wins = False
                if i+2 <= bound and game_board[i][j] == game_board[i+1][j] == game_board [i+2][j] != ' ':
                    computer_wins = True
                    if computer_wins == True:
                        break
                if j+2 <= bound and game_board[i][j] == game_board[i][j+1] == game_board [i][j+2] != ' ':
                    computer_wins = True
                    if computer_wins == True:
                        break
                if i+2 <= bound and j+2 <= bound and game_board[i][j] == game_board[i+1][j+1] == game_board [i+2][j+2] != ' ':
                    computer_wins = True
                    if computer_wins == True:
                        break
                if i-1 >= 0 and j-1 >= 0 and i+1 <= 2 and j+1 <= 2 and game_board[i-1][j+1] == game_board[i][j] == game_board[i+1][j-1] != ' ':
                    computer_wins = True
                    if computer_wins == True:
                        break

        if computer_wins == True:
            print("Computer won!")
            break

        draw = True
        for row in game_board:
            if " " in row:
                draw = False
                break
                    
        if draw == True:
            print("It's Draw!")
            break

user_number = int(input("Choose '0' or '1': "))
if user_number == 0:
    computer_number = 1
else:
    computer_number = 0
tic_tac_toe(user_number, computer_number)

    





