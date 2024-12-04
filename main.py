import library as l

print("Hello and welcome to Tik Tak Toe!")

game_on = True
p1, p2 = l.intro()

print("\nHere is how you can choose the correct spot for your mark: \n")
board = ["#","1","2","3","4","5","6","7","8","9"]

l.draw(board)

board = ["#","_","_","_","_","_","_","_","_","_"]

turn = l.choose_first()

print(f"{turn} goes first")

l.draw(board)
while game_on == True:

    if turn == "Player 1":
        selection = l.choose_symbol(board,turn)
        while selection == "occupied":
            print("This spot is occupied, choose a different one")
            selection = l.choose_symbol(board, turn)
        l.place_symbol(board,selection,p1)
        l.draw(board)
        i = l.win_check(board,p1)
        if i == True:
            print(f"{turn} wins")
            l.draw(board)
            game_on = False
        else:
            i = l.full_board_check(board)
            if i == True:
                print("It's a tie!")
                game_on = False
            else: turn = "Player 2"


    elif turn == "Player 2":
        selection = l.choose_symbol(board,turn)
        while selection == "occupied":
            print("This spot is occupied, choose a different one")
            selection = l.choose_symbol(board, turn)
        l.place_symbol(board,selection,p2)
        l.draw(board)
        i = l.win_check(board,p2)
        if i == True:
            print(f"{turn} wins")
            l.draw(board)
            game_on = False
        else:
            i = l.full_board_check(board)
            if i == True:
                print("It's a tie!")
                game_on = False
            else: turn = "Player 1"