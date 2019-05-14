currentState=[['0' for col in range(7)] for row in range(6)]
currentState[5][0]='R'
currentState[4][0]='R'
currentState[3][0]='R'
currentState[2][0]='R'
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
                result = isComplete(state[row],col,col+4)
                if result != 0:
                    return result
            if row+4 <= 6:
                print(state[row][col])
                vec=[state[row][col],state[row+1][col],state[row+2][col],state[row+3][col]]
                print(vec)
                result = isComplete(vec,0,4)
                if result != 0:
                    return result
            if (col+4 <= 7) and (row+4 <= 6):
                vec = [state[col][row],state[col+1][row+1],state[col+2][row+2],state[col+3][row+3]]
                result = isComplete(vec,0,4)
                if result != 0:
                    return result
    return '0'
            
        
##def utilityFunc(state,turn,depth):
##    baseCheck = isBaseCase(state)
##    if (baseCheck != '0'):
##        return 
#print(currentState)
print(isBaseCase(currentState))
