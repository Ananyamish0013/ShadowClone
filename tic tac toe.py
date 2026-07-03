#show board, ask player to play, insert, check if win, if not next repeat, if yes end


board = [
    ["" ,"" ,"" ],
    ["" ,"" ,"" ],
    ["" ,"" ,"" ]
]

def player():
    current_player = "X"
    row = input("Input which row(0-2): ")
    column = input("Input which column(0-2): ")
    y= input("Enter symbol(X/O): ")
    if current_player != y:
        print("Invalid symbol")
        y
    else:
        board[row][column]=y


def which_player():
    for i in range(3):
        for j in range(3):
            if board[i][j]== "":
                player()
    

def win():
    for i in range(3):
        if board[0][i] == "X":
            print("X won!")
            return
        elif board[0][i]== "O":
            print("O won!!")
            return
        elif board[1][i] == "X":
            print("X won!")
            return
        elif board[1][i]== "O":
            print("O won!!")
            return
        elif board[2][i] == "X":
            print("X won!")
            return
        elif board[2][i]== "O":
            print("O won!!")
            return
        elif board[i][0] == "X":
            print("X won!")
            return
        elif board[i][0]== "O":
            print("O won!!")
            return
        elif board[i][1] == "X":
            print("X won!")
            return
        elif board[i][1]== "O":
            print("O won!!")
            return
        elif board[i][2] == "X":
            print("X won!")
            return
        elif board[i][2]== "O":
            print("O won!!")
            return
        else:
            return

while True:
    print(board)
    which_player()
    print(board)
    win()


