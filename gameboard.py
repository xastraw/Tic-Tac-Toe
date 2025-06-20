
class Board:
    def __init__(self):
        #'''
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]
        '''
        self.board = [
            ['X', 'O', 'X'],
            ['O', '-', 'O'],
            ['O', '-', '-']
        ]
        '''
        
    def print_board(self):
        print("\ta\tb\tc")
        row_labels = ['1', '2', '3']
        for idx, row in enumerate(self.board):
            print(f"{row_labels[idx]}\t" + "\t".join(row))
        #print("\n")

    def getMove(self, player): 
        #gets the move from player and places the marker on gameboard

        #to map moves
        moves = {
            "1": 0,
            "2": 1,
            "3": 2,
            "a": 0,
            "b": 1,
            "c": 2
        }

        position = tuple(input("What row and column? Enter as coords (ex. 1a): "))
        row = moves.get(position[0])
        column = moves.get(position[1])

        if row == None or column == None:
            print("Invalid position, please choose another one.")
            self.getMove(player)
        elif self.board[row][column] != '-':
            print("Spot already taken, pick another one.")
            self.getMove(player)
        else: #Places player
            self.placePlayer(player, row, column)
    
    def placePlayer(self, player, row:int, column:int):
        self.board[row][column] = player

    
    def checkWin(self):
        #returns True if the game is over, false otherwise
        
        if self.checkColWin("X") or self.checkRowWin("X") or self.checkDiagWin("X"):
            print("\tX Wins!")
            return True
        if self.checkColWin("O") or self.checkRowWin("O") or self.checkDiagWin("O"):
            print("\tO Wins!")
            return True
        elif self.checkTie():
            print("\tIts a tie!")
            return True
        else:
            return False
        
    def checkColWin(self, marker):
        for i in range(3):
            if self.board[0][i] == marker and self.board[1][i] == marker and self.board[2][i] == marker:
                return True

    def checkRowWin(self, marker):
        for i in range(3):
            if self.board[i][0] == marker and self.board[i][1] == marker and self.board[i][2] == marker:
                return True
        
    def checkDiagWin(self, marker):
        if self.board[0][0] == marker and self.board[1][1] == marker and self.board[2][2] == marker:
            return True
        if self.board[0][2] == marker and self.board[1][1] == marker and self.board[2][0] == marker:
            return True

    def checkTie(self):
        if '-' not in self.board[0] and '-' not in self.board[1] and '-' not in self.board[2]:
            #if there are blank spaces in board it means it can't be tied yet
            return True
        return False
            
    def clearBoard(self):
        self.__init__()

