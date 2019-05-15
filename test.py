from  ai import *
from Interface import *

import pprint
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

pp = pprint.PrettyPrinter()

# Print 2D in gray scale
def colorPrint(state,  title = "figure1"):
	tempState = state
	for col in range(7):
		for row in reversed(range(6)):
			if tempState[row][col] == '0':
				tempState[row][col] = 0
			elif tempState[row][col] == 'R':
				tempState[row][col] = 1
			elif tempState[row][col] == 'G':
				tempState[row][col] = 2

	array = np.array(tempState).astype(np.uint8)
	plt.imshow(array, cmap="gray")
	plt.title(title)
	plt.show() 

# print array of 2D arrays in gray scale >> one at a time
def colorPrintSuccessor(Successor):
	for i in range(len(Successor)):
		title = "successor number" + str(i)
		colorPrint(Successor[i], title)

# Make rows and cols equal
def equal(rows, cols):
        if len(rows) < len(cols):
                for i in range(len(cols)-1):
                        rows.append(rows[0])
        elif len(rows) > len(cols):
                for i in range(len(rows)-1):
                        cols.append(cols[0])
        return rows, cols

# Create a state from rows and cols index
def makeState (rows, cols, mode = 0):
	# test mode: draw or win
    if mode == 1:
    	# draw test
        currentState=[['G' for col in range(7)] for row in range(6)]
    else:
    	# win test
    	currentState=[['0' for col in range(7)] for row in range(6)]

    # make rows and cols equal
    rows, cols = equal(rows, cols)

    # populate the 2d array
    for i in range(len(rows)):
    	currentState[rows[i]][cols[i]] = 'R'
    if mode == 1:
                i
    print("just created: ")
    pp.pprint(currentState)
    return currentState
    
# testing version of Successors()
def Successors(state,turn):
        successors=[]
        tempState= deepcopy(state)
        for col in range(7):
        	for row in reversed(range(6)):
        		#print(state)
        		if state[row][col] == '0':
        			print(row,col)
        			tempState=deepcopy(state)
        			tempState[row][col]=turn
        			successors.append(tempState)
        			break
        # get the 7 possible states out of each state: 0 to 6 using khaled's code
        print("Possible successors: ")
        #pp.pprint(successors)
        colorPrintSuccessor(successors)
        return successors



# draw and win testing function
def testBaseCase(state):          
        try:
                print("isBaseCase:", isBaseCase(state))
                #print("Successors:", Successors(state,'R'))
                #pp.pprint(Successors(state,'R'))
        except Exception as e:
                print("Test failed "+ str(e))


def testBoardInterface():
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
	            print("I'm in col", col, "and it's full")
	            row=open_row_position(board, col)
	            drop_piece(board,row,col,"G")

	    #player 2        
	    else:
	        col = int(input("choose where to play (from 0 to 6):"))

	        while col > 6 or col < 0:
	            col = int(input("choose where to play (from 0 to 6):"))  

	        if column_is_full(board, col):
	            print("I'm in col", col, "and it's full")
	            row=open_row_position(board, col)
	            drop_piece(board,row,col,"R")
	    
	    # Flip board
	    fboard = np.flip(board,0)
	    print(fboard)
	            
	    turn = turn + 1
	    turn = turn % 2

'''
print("***TESTING PRINTING BOARD IN COLORS***")
print(colorPrint([['0', '0', 'G', '0', '0', '0', '0'],
       ['0', '0', '0', '0', '0', '0', '0'],
       ['0', '0', '0', 'R', '0', '0', '0'],
       ['0', '0', 'R', '0', '0', '0', '0'],
       ['0', 'R', '0', '0', '0', '0', '0'],
       ['R', '0', '0', '0', '0', 'R', '0']]))


print("***TESTING ROW***")
testBaseCase(makeState([0], [1,2,3,4]))

print("***TESTING ROW***")
testBaseCase(makeState([1], [2,3,4]))

print("***TESTING ROW***")
testBaseCase(makeState([4], [2,3,4,5]))

print("***TESTING COLUMN***")
testBaseCase(makeState([0,1,3,2], [1]))

print("***TESTING COLUMN***")
testBaseCase(makeState([2,3,4,5], [3]))

print("***TESTING DIAGONAL***")
testBaseCase(makeState([5,4,3,2], [0,1,2,3]))

print("***TESTING DIAGONAL***")
testBaseCase(makeState([2,3,4,5], [0,1,2,3]))


print("***TESTING DRAW***")
testBaseCase(makeState([0,0,0,1,1,1,1,2,2,2,3,3,3,3,3,4,4,5,5,5,5],
         [1,2,4,0,1,3,5,3,5,6,0,1,2,4,5,3,4,0,1,4,5], 1))


print("***TESTING SUCCESSORS***")
Successors(makeState([5,4,3,2], [4,1,2,3]), 'R')
'''

testBoardInterface()