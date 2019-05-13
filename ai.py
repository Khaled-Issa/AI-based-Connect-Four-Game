currentState=[['0' for col in range(7)] for row in range(6)]
def isComplete(row,start,end):
    for i in range(start,end):
        if row[i]!=row[i-1]:
            return 0
    return row[0]
def isBaseCase(state):
    for row in range(6):
        for col in range(7):
            if state[row][col] == '0':
                continue
            if col+4 < 7:
                result = isComplete(state[row],col,col+4)
                if result != 0:
                    return result
            if row+4 < 6:
                result = isComplete(state[col],row,row+4)
                if result != 0:
                    return result
            if (col+4 < 7) and (row+4 < 6):
                vec = [state[col][row],state[col+1][row+1],state[col+2][row+2],state[col+3][row+3],state[col+4][row+4]]
                result = isComplete(vec,0,4)
                if result != 0:
                    return result
    return '0'
            
        
def utilityFunc(state,turn,depth):
    baseCheck = isBaseCase(state)
    if (baseCheck != '0'):
        return 
