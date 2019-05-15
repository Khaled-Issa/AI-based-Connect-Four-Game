import pprint
from  ai import *

def Successors(state,turn):
        successors=[]
        tempState=state
        for col in range(7):
                for row in range(6):
                        if state[row][col] == '0':
                                tempState=state
                                tempState[row][col]=turn
                                successors.append(tempState)
                                tempState[row][col]='0'
                                #print(row,col)
                                #Move to the next column
                                break
        # get the 7 possible states out of each state: 0 to 6 using khaled's code
        return successors
# make rows and cols equal
def equal(rows, cols):
        if len(rows) < len(cols):
                for i in range(len(cols)-1):
                        rows.append(rows[0])
        elif len(rows) > len(cols):
                for i in range(len(rows)-1):
                        cols.append(cols[0])
        return rows, cols

# draw and win testing function
def test(rows, cols, mode = 0):
        pp = pprint.PrettyPrinter()
        # test mode: draw or win
        if mode == 1:
                # draw test
                currentState=[['G' for col in range(7)] for row in range(6)]
        else:
                # win test
                currentState=[['0' for col in range(7)] for row in range(6)]

        # make rows and cols equal
        rows, cols = equal(rows, cols)

        for i in range(len(rows)):
                currentState[rows[i]][cols[i]] = 'R'
        pp.pprint(currentState)

        if mode == 1:
                i
        try:
                #print("isBaseCase:", isBaseCase(currentState))
                #print("Successors:", Successors(currentState,'R'))
                pp.pprint(Successors(currentState,'R'))
        except Exception as e:
                print("Test failed "+ str(e))



print("***TESTING ROW***")
test([0], [1,2,3,4])

print("***TESTING ROW***")
test([1], [2,3,4])

print("***TESTING ROW***")
test([4], [2,3,4,5])

print("***TESTING COLUMN***")
test([0,1,3,2], [1])

print("***TESTING COLUMN***")
test([2,3,4,5], [3])

print("***TESTING DIAGONAL***")
test([5,4,3,2], [0,1,2,3])

print("***TESTING DIAGONAL***")
test([2,3,4,5], [0,1,2,3])

print("***TESTING DRAW***")
test([0,0,0,1,1,1,1,2,2,2,3,3,3,3,3,4,4,5,5,5,5],
         [1,2,4,0,1,3,5,3,5,6,0,1,2,4,5,3,4,0,1,4,5], 1)

