from gameboard import Board    

def playAgain(b):    
    play = str(input("Play again? Y/N "))
    if play == "Y" or play == "y":
        print("\n")
        b.clearBoard()
        b.print_board()
        return True
    
    else:
        return False

    
def main():
    b = Board()
    player = "X" #X goes first
    ogPlayer = player
    b.print_board()

    while True:
        print(f"\tPlayer {player}'s turn!")
        b.getMove(player)
        b.print_board()

        if b.checkWin()== True:
            if playAgain(b):
                ogPlayer = "O" if ogPlayer == "X" else "X" 
                player = ogPlayer
            else:
                break
        else:
            #swaps player at each turn
            player = "O" if player == "X" else "X"

main()

