
board=[
    ['-', '-', '-'], 
    ['-', '-', '-'], 
    ['-', '-', '-']
]

player = "o"


def print_board():
    print("\n")
    print("\t0\t\t1\t\t2")
    count = 1
    
    
    for row in board:
        tempBoard = ""
        for col in row:
            tempBoard += "\t" + col + "\t"
        print(count, tempBoard + "\n")
        count+= 1
    
def placePlayer(player):
    row=2
    col=2
    board[row][col] = player
    print_board()
    if player == "x":
        player = "o"
    else:
        player = "x"
    print(player)



print_board()
placePlayer(player)

