import random

def draw(board):

    print(f" {board[1]} | {board[2]} | {board[3]}")
    print("___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("___|___|___")
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print("")

def intro():

    pl_input = input("Player 1, choose your symbol (x or o): ")
    while pl_input not in ("x", "o"):
        pl_input = input("Choose the correct entry: ")
    if pl_input == "x":
        print(f"Player 2, your symbol is o then")
        return ("x","o")
    elif pl_input == "o":
        print("Player 2, your symbol is x then")
        return ("o","x")

def place_symbol(board, position, symbol):

    board[position] = symbol

def win_check(board, mark):

    if board[1] == mark and board[2] == mark and board[3] == mark:
        board[1] = mark.upper()
        board[2] = mark.upper()
        board[3] = mark.upper()
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        board[4] = mark.upper()
        board[5] = mark.upper()
        board[6] = mark.upper()
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        board[7] = mark.upper()
        board[8] = mark.upper()
        board[9] = mark.upper()
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        board[1] = mark.upper()
        board[5] = mark.upper()
        board[9] = mark.upper()
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        board[3] = mark.upper()
        board[5] = mark.upper()
        board[7] = mark.upper()
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        board[1] = mark.upper()
        board[4] = mark.upper()
        board[7] = mark.upper()
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        board[2] = mark.upper()
        board[5] = mark.upper()
        board[8] = mark.upper()
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        board[3] = mark.upper()
        board[6] = mark.upper()
        board[9] = mark.upper()
        return True

def full_board_check(board):

    i = 1
    m = 0
    for i in range(1,10):
        if board[i] == "_":
            m +=1
        i +=1
    if m == 0:
        return True
    else: return False

def space_check(board, position):

    if board[position] == "_":
        return True
    else: return False

def choose_symbol(board, player):

    acceptable_range = range(1,10)
    choice = "wrong"
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input(f"{player}, choose a spot (1-9): ")

        if choice.isdigit() == False:
            print("Wrong input, please try again")
        elif choice.isdigit() == True:
            if int(choice) in acceptable_range:
                new_position = int(choice)
                break
            print("Wrong input, please try again")

    check = space_check(board, new_position)
    if check == True:
        return new_position
    else:
        return "occupied"

def choose_first():
    choice = random.choice([1,2])

    if choice == 1:
        return "Player 1"
    else: return "Player 2"