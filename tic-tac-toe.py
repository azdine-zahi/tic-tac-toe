import random

board = ["_"] * 9
player = "X"
AI = False

def display_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def handle_turn(player):
    if AI and player == 'O':
        position = ai_turn()
    else:
        print(player + "'s turn.")
        position = input("Choose a position from 1-9: ")

        valid = False
        while not valid:
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Choose a position from 1-9: ")

            position = int(position) - 1

            if board[position] == "_":
                valid = True
            else:
                print("You can't go there. Go again.")

    board[position] = player

    display_board()

def ai_turn():
    position = random.randint(0,8)
    while board[position] != "_":
        position = random.randint(0,8)
    print("AI's turn.")
    print("AI chose position: ", position + 1)
    return position

def check_for_win():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
   
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_for_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
        return True
    return False

def flip_player():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

play_game = input("Do you want to play a game of Tic Tac Toe? (y/n)")

if play_game == "y":
    game_mode = input("Do you want to play against another player or an AI? (p/a)")
    if game_mode == "a":
        AI = True
    game_still_going = True
    display_board()
    while game_still_going:
        handle_turn(player)
        check_for_win()
        check_for_tie()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
else:
    print("Ok, bye!")
