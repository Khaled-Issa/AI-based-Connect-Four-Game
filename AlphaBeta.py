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
        #print("I'm in the Min Value - beginning")
        utility = isBaseCase(state)
        if utility != "0":
                return ord(utility)
        
        value = INF

        # loop in all successors/children
        successors_path=Successors(state,'G')
        for childState, move in zip(successors_path[0],successors_path[1]):
                #print("I'm in loop min value - beginning")
                path.append(move)
                maxValue = MaxValue(childState, Alpha, Beta, path)
                value = min(value, maxValue)
                if value <= Alpha:
                        return value
                ###I dont' know what is that doing
                Beta = min(Beta, value)
                #print("I'm in loop min value - end")
        #print("I'm in min value")
        return value

# return the max value of this state
def MaxValue(state, Alpha, Beta,path):
        # Check if the current state is a terminal one "win/draw"
        # if yes return the utitilty "R/G/0"
        #print("I'm in max value - beginning")
        utility = isBaseCase(state)
        #print("utility = ", utility)
        if utility != "0":
                return ord(utility)
        
        value = NEGINF

        # loop in all successors/children
        successors_path=Successors(state,'R')
        for childState, move in zip(successors_path[0],successors_path[1]):
                #input("I'm in loop max value - beginning")
                path.append(move)
                minValue = MinValue(childState,Alpha,Beta, path)
                value = max(value, minValue)
                if value >= Beta:
                        return value
                ###I dont' know what is that doing
                Alpha = max(Alpha, value)
                #input("I'm in loop Max Value - end")
        #pretty_print(state)
        #print(Alpha)
        #print(Beta)
        #input("I'm in max value - end")
        #print(value)
        return value

# return action to the Interface function
def AlphaBeta():
        # Playing Logic
        board = make_board()
        pboard=np.array(board)

        no_winner = True
        turn = 0 
        v = 0

        
        while no_winner:
            #player 1
            if turn == 0:
                col = int(input("choose where to play (from 0 to 6):"))

                while col > 6 or col < 0:
                    col = int(input("choose where to play (from 0 to 6):"))

                if column_is_not_full(board, col):
                    row= open_row_position(board, col)
                    drop_piece(board, row, col, "G")
                #print("I'm in player One")
   
            else:
                # player 2 >> CHANGE THE 2ND PLAYER TO BOARD
                # Tree, Alpha Beta pruning
                #print()
                print("I'm in player two - beginning")
                path=[]
                v = MaxValue(board, NEGINF,INF ,path)
                print(path,1)
                # IS V the brnahes value ? Nope
                # CREATE ACTION HERE
                if column_is_not_full(board, col):
                        row=open_row_position(board, col)
                        drop_piece(board,row,col,"R")
                #print()
                #print("I'm in player two - end")
            
            # Flip board
            fboard = np.flip(board,0)
            print(fboard)
            #print(v, v == 71)
            if(v == '71'):
            	no_winner = False
            # switch turn       
            turn = turn + 1
            turn = turn % 2
            # wait for imput from user
            #print("I'm in AlphaBeta")

          


AlphaBeta()
