board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
Player = "X"
winner = None
gameRunning = True

#printing board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input
def playerInput(board):
    while True:
        if Player == "X":
            inp = int(input(f"Enter a number 1-9 \033[1;34m Player (X) \033[0;0m : "))
        else:
            inp = int(input(f"Enter a number 1-9 \033[1;31m Player (0) \033[0;0m : "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = Player
            break
        else:
            if Player == "X":
                print(f" Try again! Player - \033[1;34m Player (X) \033[0;0m ! ")
            else:
                print(f" Try again! Player - \033[1;31m Player (0) \033[0;0m ! ")
            printBoard(board)


#check for win or tie
def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = Player
        return True
def checkRow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = Player
        return True
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = Player
        return True
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Its a tie")
        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")

#switch the player
def switchPlayer():
    global Player
    if Player == "X":
        Player = "O"
    else:
        Player = "X"



#check for win or tie again

while gameRunning:
    printBoard(board)
    if winner != None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()