'''
board=[
    #0     1    2
    ['-', '-', '-'],    #0
    ['-', '-', '-'],    #1
    ['-', '-', '-']     #2
]#'''

player = "X"
bot = "O"


#'''
board = [
    [ 'X', 'O', 'X' ], 
    [ 'O', 'O', 'X' ], 
    [ '-', '-', '-' ] 
]#'''

def printBoard():
    print("\t1\t\t2\t\t3\n")
    count = 1
    
    for row in board:
        tempboard = ""
        for col in row:
            tempboard = tempboard + "\t" + col +"\t"
        print(count, tempboard, "\n")
        count = count+1

def takeTurn():
    col = int(input("Please pick a column: "))
    row = int(input("Please pick a row: "))
    col = col-1     #subtract 1 because python starts at 0
    row = row-1    
    if isValidMove(row, col) == True:
        board[row][col] = player
    else:
        takeTurn()

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

def checkTie():
    if '-' in board[0] or '-' in board[1] or '-' in board[2]:       
        #if there are blank spaces in board it means it can't be tied yet
        return False
    else:
        return True
 
def checkWin():
    #only checks for the player, not the bot
    for row in range(3):    #check row wins
        if(board[row][0] == player and board[row][1] == player and board[row][2] == player):
            return True
        
    for col in range(3):    #check col win
        if(board[0][col] == player and board[1][col] == player and board[2][col] == player):
            return True
    
    #check diag wins
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

def checkAiWin():
    #checks the win for the bot

    for row in range(3):    #check row wins
        if(board[row][0] == bot and board[row][1] == bot and board[row][2] == bot):
            return True
        
    #check col win
    for col in range(3):    
        if(board[0][col] == bot and board[1][col] == bot and board[2][col] == bot):
            return True
    
    #check diag wins
    if board[0][0] == bot and board[1][1] == bot and board[2][2] == bot:
        return True
    if board[0][2] == bot and board[1][1] == bot and board[2][0] == bot:
        return True



def minimax(board, isMax, depth):

    if checkWin == True:
        #player wins which we dont want so return negative score
        return -10            
    elif checkAiWin == True:
        #bot wins which we want so return positive score
        return 10
    elif checkTie() == True:
        #its a draw so return 0 score
        return 0


    if (isMax):
        best = -1000
        print("if statement")
        for i in range(3):
            for j in range(3):

                if board[i][j] == '-':
                    board[i][j] = bot

                    best = max(best, minimax(board, not isMax))

                    board[i][j] = "-"
        return best
    else:
        best = 1000
        print("else statement")
        for i in range(3):
            for j in range(3):

                if board[i][j] == '-':
                    board[i][j] = player

                    best = min(best, minimax(board, not isMax))

                    board[i][j] = "-"
        
        return best


def findBestMove(board):
    bestval = -10000
    bestMove = (-1,-1)

    #goes through every cell and does minimax on every single empty cell
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':

                board[i][j] = bot

                moveval = minimax(board, False, 0)

                board[i][j] = '-'

                if (moveval > bestval):
                    bestMove = (i,j)
                    bestval = moveval
    return bestMove



def gameGoing():    #function that runs the game

    gameOn = True
    whoTurn = player

    while gameOn == True:

        print("-----------------------------------------")#helps with viewing

        if whoTurn == player:
            print("Your turn!")
            takeTurn()
        else:
            print("Bot's Turn!")
            bestmove  = findBestMove(board)
            print("Bot chosen row: ", bestmove[0]+1)
            print("Bot chosen column: ", bestmove[1]+1)
            board[bestmove[0]][bestmove[1]] = bot

        
        print("\n")
        printBoard()
        
        #checks to see if someone won
        if checkWin() == True:
            print("\t\tYou win!")
            gameOn = False
        elif checkAiWin() == True:
            print("\t\tBot wins!")
            gameOn = False
        elif checkTie() == True:
            print("\t\t    Its a tie!")
            gameOn = False
        
        #switches player
        if whoTurn == player:
            whoTurn = bot
        else:
            whoTurn = player


def main():

    print("\n")
    print("\t   Welcome to Tic-Tac-Toe!")
    print("\n")
    printBoard()

    gameGoing()



main()