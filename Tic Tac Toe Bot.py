'''
board=[
    #0     1    2
    ['-', '-', '-'],    #0
    ['-', '-', '-'],    #1
    ['-', '-', '-']     #2
]'''
board =[]

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


    if play == "X":
        col = int(input("Player " + play + ", please pick a col. "))
        row = int(input("Player " + play + ", please pick a row. "))
        row = row-1    #subtract 1 because python starts at 0
        col = col-1
        if isValidMove(row, col) == True:
            placePlayer(play, row, col)
        else:
            takeTurn(play)

    elif play == "O":
        miniMax("O")
    
    

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


def checkColWin(play):
    for i in range(3):
        if board[0][i] == play and board[1][i] == play and board[2][i] == play:
            return True
    

def checkRowWin(play):
    for i in range(3):
        if board[i][0] == play and board[i][1] == play and board[i][2] == play:
            return True

            
def checkDiagWin(play):
    if board[0][0] == play and board[1][1] == play and board[2][2] == play:
        return True
    if board[0][2] == play and board[1][1] == play and board[2][0] == play:
        return True

def checkTie():
    if '-' in board[0] or '-' in board[1] or '-' in board[2]:       #if there are blank spaces in board it means it can't be tied yet
        return False
    else:
        return True

def checkWin(player):

    if (checkRowWin(player) or checkColWin(player) or checkDiagWin(player)):
        return True

    '''
    if (checkRowWin("X") or checkColWin("X") or checkDiagWin("X")) == True:
        print("\t\t     X Wins!")
        return True         #returning true so main function knows to end the game
    elif (checkRowWin("O") or checkColWin("O") or checkDiagWin("O")) == True:
        print("\t\t     O Wins!")
        return True
    elif(checkTie() == True):
        print("\t\t   It's a tie!")
        return True
    '''


def miniMax(player):
    
    optimalRow = -1 
    optimalCol = -1
    moves =[]
    if checkWin("X") == True:           #dont want to happen so negative score returned
        #print("results in X winning")
        return (-10, None, None)              
    elif checkWin("O") == True:         #want to happen so positive score
        #print("results in O winning")
        return (10, None, None)
    elif checkTie() == True:            #draw so no score attributed
        #print("results in a tie")
        return (0, None, None)



    if player == "O":
        best = -1000
        #for every avaible space place O, then run max function, then return board to original state
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    placePlayer("O", row, col)
                    print(row, col)
                    bestScore = max(best, miniMax("X")[0])   
                    #what this does is find the highest number between the value of best(-1000) and miniMax(could be legit -20 or 60) idea is that -1000 is so low it will never reach
                    placePlayer("-", row, col)
        optimalRow = row
        optimalCol = col
        return (bestScore, optimalRow, optimalCol)

    if player == "X":
        worst = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    placePlayer("X", row, col)
                    print(row, col)
                    worstScore = min(worst, miniMax("O")[0])
                    placePlayer("-", row, col)
        optimalRow = row
        optimalCol = col
        return (worstScore, optimalCol, optimalRow)

def main():

    print("\n")
    print("\t   Welcome to Tic-Tac-Toe!")
    #printBoard()
    print("\n\n\n")

    player = "O"
    gameOn = False
        
    board.append(["O","X","-"])
    board.append(["-","X","-"])
    board.append(["-","-","-"])
    print("Calling minimax('O') on this board:")
    printBoard()
    print("Minimax should return (0, 2, 1):", miniMax("O"))

    while gameOn == True:
        print("Player " + player + "'s Turn")
        takeTurn(player)
        

        if checkWin("X") == True:
            gameOn = False
        elif checkWin("Y") == True:
            gameOn = False

        if player == "X":
            player = "O"
        else:
            player = "X"


main()
