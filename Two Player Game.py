import numpy as np

def make_board():
    rows, columns = 6, 7
    board = [[0 for x in range(columns)] for y in range(rows)]
    #board=np.zeros((6,7))
    return board

def drop_piece(board,row,column,piece):
    board[row][column]=piece

def column_is_full(board,col):
    return board[5][col] == 0

def open_row_position(board,col):
    for rp in range(6):
        if board[rp][col] == 0:
            return rp   

def pretty_print(pboard):
    print(np.flip(board,0))
   

board = make_board()
pboard=np.array(board)

no_winner = True
turn = 0 

pretty_print(pboard)

while no_winner:
    #player 1
    if turn == 0:
        col = int(input("choose where to play (from 0 to 6):"))

        while col > 6 or col < 0:
            col = int(input("choose where to play (from 0 to 6):"))

        if column_is_full(board, col):
            row= open_row_position(board, col)
            drop_piece(board, row, col, "G")

    #player 2        
    else:
        col = int(input("choose where to play (from 0 to 6):"))

        while col > 6 or col < 0:
            col = int(input("choose where to play (from 0 to 6):"))  

        if column_is_full(board, col):
            row=open_row_position(board, col)
            drop_piece(board,row,col,"R")
    
    # Flip board
    fboard = np.flip(board,0)
    print(fboard)
            
    turn = turn + 1
    turn = turn % 2    
    

#fboard=np.asanyarray(board)   
