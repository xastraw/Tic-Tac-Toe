'''
board=[
    #0     1    2
    ['-', '-', '-'],    #0
    ['-', '-', '-'],    #1
    ['-', '-', '-']     #2
]'''
#'''
board = [
    [ 'X', 'O', 'X' ], 
    [ 'O', 'O', 'X' ], 
    [ '-', '-', '-' ] 
]#'''
#game state get cahnges = problem

player = "O"
#should be X by default
game_on = True
#make true to have game go

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
        col = int(input("Player " + play + ", please pick a col: "))
        row = int(input("Player " + play + ", please pick a row: "))
        row = row-1    #subtract 1 because python starts at 0
        col = col-1
        if isValidMove(row, col) == True:
            placePlayer(board, play, row, col)
        else:
            takeTurn(play)

    elif play == "O":
        getBestMove(board)

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


def placePlayer(game, play,r,c):
    game[r][c] = play
    return game #returns the game board so that the minimax function can see what the new game board looks like


def checkTie(game):
    if '-' in game[0] or '-' in game[1] or '-' in game[2]:       #if there are blank spaces in game it means it can't be tied yet
        return False
    else:
        return True

def checkWin(game, play):
    #check col win
    for i in range(3):
        if game[0][i] == play and game[1][i] == play and game[2][i] == play:
            return True

    #check row win
    for i in range(3):
        if game[i][0] == play and game[i][1] == play and game[i][2] == play:
            return True
    
    #check diag win
    if game[0][0] == play and game[1][1] == play and game[2][2] == play:
        return True
    if game[0][2] == play and game[1][1] == play and game[2][0] == play:
        return True



def getPossibleMoves(game):
    for r in range(3):
        for c in range(3):
            if '-' in game[r][c]:
                return r,c


def getBestMove(game_state):
    #game_state is the current board state
    def minimax(state, player, depth):
            #state is the board but we are modifying it
            #o is bot
            #x is player
            if checkWin(state, 'O'):  # bot wins
                return 10
            elif checkWin(state, 'X'):  # opponent wins
                return -10
            elif checkTie(state):  # draw
                return 0

            if player == 'O':
                best_score = -1000
                for blank in getPossibleMoves(state):
                    move = getPossibleMoves(state)
                    print(move)
                    print(type(move))
                    new_state = placePlayer(state, player, move[0], move[1])
                    score = minimax(new_state, 'X', depth+1)
                    best_score = max(best_score, score)
                return best_score
            else:
                best_score = 1000
                for blank in getPossibleMoves(state):
                    move = getPossibleMoves(state)
                    new_state = placePlayer(state, player, move[0], move[1])
                    score = minimax(new_state, 'O', depth+1)
                    best_score = min(best_score, score)
                return best_score



    # main function logic
    #from chatgpt: x is the bot and O is the player
    best_score = -1000
    best_move = None
    for blank in getPossibleMoves(game_state):
        move = getPossibleMoves(game_state)
        new_state = game_state  #doing this so we dont actually modify the game board and can keep them seperate
        new_state = placePlayer(new_state, 'O', move[0], move[1])
        score = minimax(new_state, 'X', 0)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def main():

    print("\n")
    print("\t   Welcome to Tic-Tac-Toe!")
    

    global player
    global game_on
        

    while game_on == True:
        printBoard()
        print("Player " + player + "'s Turn")
        takeTurn(player)
        

        if checkWin(board, player) == True:
            printBoard()
            print("Player ", player, " Wins!")
            game_on = False
        elif checkTie(board) == True:
            print("It's a tie!")
            game_on = False

        if player == "X":
            player = "O"
        else:
            player = "X"

        


main()
