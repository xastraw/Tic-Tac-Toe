
board=[
    #0     1    2
    ['-', '-', '-'],    #0
    ['-', '-', '-'],    #1
    ['-', '-', '-']     #2
]


player = "X"
game_on = True


def printBoard():
    print("\n")
    print("\t1\t\t2\t\t3\n")
    count = 1
    
    for row in board:
        tempboard = ""
        for col in row:
            tempboard = tempboard + "\t" + col +"\t"
        print(count, tempboard, "\n")
        count = count+1

def takeTurn(play):

    col = int(input("Player " + play + ", please pick a col: "))
    row = int(input("Player " + play + ", please pick a row: "))
    row = row-1    #subtract 1 because python starts at 0
    col = col-1
    
    if isValidMove(row, col) == True:
        placePlayer(play, row, col)
    else:
        takeTurn(play)

def isValidMove(r, c):
    
    if r <= 2 and r >= 0 and c <= 2 and c >= 0:
        if board[r][c] ==  "-":
            return True
        else:
            print("That spot is already taken, plase choose another one. ")
            return False
    else:
        print("Please pick a number between 1 and 3. ")
        return False


def placePlayer(play,r,c):
    board[r][c] = play
    printBoard()
    

def checkTie():
    if '-' in board[0] or '-' in board[1] or '-' in board[2]:
        return False
    else:
        return True

def checkWin(play):
    
    #check col win
    for i in range(3):
        if board[0][i] == play and board[1][i] == play and board[2][i] == play:
            return True
    #check row win
    for i in range(3):
        if board[i][0] == play and board[i][1] == play and board[i][2] == play:
            return True
    #check diag win
    if board[0][0] == play and board[1][1] == play and board[2][2] == play:
        return True
    if board[0][2] == play and board[1][1] == play and board[2][0] == play:
        return True


def main():

    print("\n")
    print("\t   Welcome to Tic-Tac-Toe!")
 

    global game_on
    global player

    while game_on == True:
        printBoard()
        print("Player " + player + "'s Turn")
        takeTurn(player)
        

        if checkWin(player) == True:
            printBoard()
            print("Player ", player, " Wins!")
            game_on = False
        elif checkTie() == True:
            print("It's a tie!")
            game_on = False


        if player == "X":
            player = "O"
        else:
            player = "X"


main()
