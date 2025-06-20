from gameboard import Board

def evaluate(b, player="X", bot="O"):
    # col wins
    for i in range(3):
        if b[0][i] == player and b[1][i] == player and b[2][i] == player:
            return -10
        if b[0][i] == bot and b[1][i] == bot and b[2][i] == bot:
            return 10

    # row wins
    for i in range(3):
        if b[i][0] == player and b[i][1] == player and b[i][2] == player:
            return -10
        if b[i][0] == bot and b[i][1] == bot and b[i][2] == bot:
            return 10

    # diag wins
    if b[0][0] == player and b[1][1] == player and b[2][2] == player:
        return -10
    if b[0][2] == player and b[1][1] == player and b[2][0] == player:
        return -10
    if b[0][0] == bot and b[1][1] == bot and b[2][2] == bot:
        return 10
    if b[0][2] == bot and b[1][1] == bot and b[2][0] == bot:
        return 10

    return 0

def check_tie(b):
    for row in b:
        if '-' in row:
            return False
    return True

def minimax(board, is_max, player="X", bot="O"):
    score = evaluate(board.board, player, bot)

    if score == 10 or score == -10:
        return score

    if check_tie(board.board):
        return 0

    if is_max:#for the bot
        value = -1000
        for row in range(3):
            for col in range(3):
                if board.board[row][col] == '-':
                    board.placePlayer(bot, row, col)
                    value = max(value, minimax(board, False, player, bot))

                    board.placePlayer('-', row, col)
        return value
    else:
        value = 1000
        for row in range(3):
            for col in range(3):
                if board.board[row][col] == '-':
                    board.placePlayer(player, row, col)
                    value = min(value, minimax(board, True, player, bot))
                    board.placePlayer('-', row, col)
        return value


def findBestMove(board):
    bestVal = -100
    bestMove = (-1,-1)
    bot = "O"

    for i in range(3):
        for j in range(3):
            if (board.board[i][j] == '-'):
                board.placePlayer(bot, i, j)

                minmaxVal = minimax(board, False)

                board.placePlayer('-', i, j)


                if (minmaxVal > bestVal):
                    bestMove = (i,j)
                    bestVal = minmaxVal
    
    #print(f"Best move is: ({bestMove[0] +1},{bestMove[1] +1})")
    return bestMove