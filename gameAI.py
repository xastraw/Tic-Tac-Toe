from gameboard import Board    
import minimax as mini

def playAgain(b):    
    play = str(input("Play again? Y/N "))
    if play == "Y" or play == "y":
        print("\n")
        b.clearBoard()
        b.print_board()
        return True
    
    else:
        return False
    

def mainAI():
    b = Board()
    player = "X"
    ogPlayer = player
    b.print_board()
    
    while True:
        if player == "X": #players turn
            print("\tPlayer X's turn!")
            b.getMove(player)
            b.print_board()

        else: #bot turn
            print("\tBot's turn!")
            botMove = mini.findBestMove(b)
            b.placePlayer("O", botMove[0], botMove[1])
            b.print_board()
        
        if b.checkWin()== True:
            if playAgain(b):
                #changes the starting player at a restart, nescessary to see who started originally
                ogPlayer = "O" if ogPlayer == "X" else "X" 
                player = ogPlayer
                continue
            else:
                break
        else:
            player = "O" if player == "X" else "X"
        
        

mainAI()