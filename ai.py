currentState=[['0' for col in range(7)] for row in range(6)]

currentState[5][2]='R'
currentState[4][3]='R'
currentState[3][4]='R'
currentState[2][5]='R'

def column_is_not_full(board,col):
    return board[5][col] == 0
    
def isFull(board):
    for i in range(7):
        if not column_is_not_full(board,i):
            return False
    return True
def isComplete(row,start,end):
    for i in range(start+1,end):
        if row[i]!=row[i-1]:
            return 0
    return row[0]
def isBaseCase(state):
    for row in range(6):
        for col in range(7):
            if state[row][col] == '0':
                continue
            if col+4 <= 7:
                vec=[state[row][col],state[row][col+1],state[row][col+2],state[row][col+3]]
                result = isComplete(vec,0,4)
                if result != 0:
                    return result
            if row+4 <= 6:
                vec=[state[row][col],state[row+1][col],state[row+2][col],state[row+3][col]]
                result = isComplete(vec,0,4)
                if result != 0:
                    return result
            if (col+4 <= 7) and (row+4 <= 6):
                vec = [state[row][col],state[row+1][col+1],state[row+2][col+2],state[row+3][col+3]]
                result = isComplete(vec,0,4)
                if result != 0:
                    return result
            if (col-3 >= 0) and (row+4 <= 6):
                print(row,col)
                vec = [state[row][col],state[row+1][col-1],state[row+2][col-2],state[row+3][col-3]]
                result = isComplete(vec,0,4)
                if result != 0:
                    return result
    if isFull(state):
        return 'D'
    return '0'
            
        
##def utilityFunc(state,turn,depth):
##    baseCheck = isBaseCase(state)
##    if (baseCheck != '0'):
##        return 
#print(currentState)
#print(isBaseCase(currentState))
