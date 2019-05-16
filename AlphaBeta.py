from ai import *
from Interface import *

import pprint
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
INF = 100000
NEGINF = -1
# return all the state successors
def Successors(state, turn):
        successors = []
        moves=[]
        tempState = deepcopy(state)
        for col in range(7):
                for row in range(6):
                        if state[row][col] == '0':
                                tempState = deepcopy(state)
                                tempState [row][col] = turn
                                successors.append(tempState)
                                moves.append(col)
                                break
        ###A list containing the direct children of the state as the first element
        ###And the move 
        successor_Path=[successors,moves]
        return successor_Path
# return the minmum value of this state
def MinValue(state, Alpha, Beta,path):
        # Check if the current state is a terminal one "win/draw"
        # if yes return the utitilty "R/G/0"
        utility = isBaseCase(state)
        if utility != "0":
                return ord(utility)
        
        value = INF

        # loop in all successors/children
        successors_path=Successors(state,'G')
        for childState, move in zip(successors_path[0],successors_path[1]):
                path.append(move)
                maxValue = MaxValue(childState, Alpha, Beta, path)
                value = min(value, maxValue)
                if value <= Alpha:
                        return value
                ###I dont' know what is that doing
                Beta = max(Beta, value)
        return value

# return the max value of this state
def MaxValue(state, Alpha, Beta,path):
        # Check if the current state is a terminal one "win/draw"
        # if yes return the utitilty "R/G/0"
        utility = isBaseCase(state)
        if utility != "0":
                return ord(utility)
        
        value = NEGINF

        # loop in all successors/children
        successors_path=Successors(state,'R')
        for childState, move in zip(successors_path[0],successors_path[1]):
                path.append(move)
                minValue = MinValue(childState,Alpha,Beta, path)
                value = max(value, minValue)
                if value >= Beta:
                        return value
                ###I dont' know what is that doing
                Alpha = max(Alpha, value)
        pretty_print(state)
        print(Alpha)
        print(Beta)
        return value

# return action to the Interface function >> NOT DONE YET
def AlphaBeta():
        # Playing Logic
        board = make_board()
        pboard=np.array(board)

        no_winner = True
        turn = 0 

        
        while no_winner:
            #player 1
            if turn == 0:
                col = int(input("choose where to play (from 0 to 6):"))

                while col > 6 or col < 0:
                    col = int(input("choose where to play (from 0 to 6):"))

                if column_is_not_full(board, col):
                    row= open_row_position(board, col)
                    drop_piece(board, row, col, "G")
   
            else:
                # player 2 >> CHANGE THE 2ND PLAYER TO BOARD
                # Tree, Alpha Beta pruning
                path=[]
                v = MaxValue(board, NEGINF,INF ,path)
                print(path,1)
                # IS V the brnahes value ? Nope
                # CREATE ACTION HERE
                if column_is_not_full(board, col):
                        row=open_row_position(board, col)
                        drop_piece(board,row,col,"R")
            
            # Flip board
            fboard = np.flip(board,0)
            print(fboard)
            
            # switch turn       
            turn = turn + 1
            turn = turn % 2

          


AlphaBeta()
