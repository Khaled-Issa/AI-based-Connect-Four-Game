import pprint
from  ai import *
import numpy as np
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter()

def colorPrint(state,  title = "figure1"):
	for col in range(7):
		for row in reversed(range(6)):
			if state[row][col] == '0':
				state[row][col] = 0
			elif state[row][col] == 'R':
				state[row][col] = 1
			elif state[row][col] == 'G':
				state[row][col] = 2

	array = np.array(state).astype(np.uint8)
	plt.imshow(array, cmap="gray")
	plt.title(title)
	plt.show() 

def colorPrintSuccessor(Successor):
	for i in range(len(Successor)):
		title = "successor number" + str(i)
		colorPrint(Successor[i], title)

# make rows and cols equal
def equal(rows, cols):
        if len(rows) < len(cols):
                for i in range(len(cols)-1):
                        rows.append(rows[0])
        elif len(rows) > len(cols):
                for i in range(len(rows)-1):
                        cols.append(cols[0])
        return rows, cols

# create aa state from rows and cols index
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
    


def Successors(state,turn):
        successors=[]
        tempState=state
        for col in range(7):
        	for row in reversed(range(6)):
        		if state[row][col] == '0':
        			#print(row,col)
        			tempState=state
        			tempState[row][col]=turn
        			#pp.pprint(tempState)
        			successors.append(tempState)
        			#print("Successors: ")
        			#pp.pprint(successors)
        			tempState[row][col]='0'
        			
        			#Move to the next column
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


def testSuccesors(rows, cols):
	pp = pprint.PrettyPrinter()
	#currentState = [['0' for]]
'''
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

'''
print("***TESTING PRINTING BOARD IN COLORS***")
print(colorPrint([['0', '0', 'G', '0', '0', '0', '0'],
       ['0', '0', '0', '0', '0', '0', '0'],
       ['0', '0', '0', 'R', '0', '0', '0'],
       ['0', '0', 'R', '0', '0', '0', '0'],
       ['0', 'R', '0', '0', '0', '0', '0'],
       ['R', '0', '0', '0', '0', 'R', '0']]))

print("***TESTING SUCCESSORS***")

Successors(makeState([5,4,3,2], [0,1,2,3]), 'R')

