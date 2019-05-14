import ai
import Interface

# return all the state successors
def Successors(state):
	successors = []
	return successors

# return the minmum value of this state
def MinValue(state, Alpha, Beta):
	# Check if the current state is a terminal one "win/draw"
	# if yes return the utitilty "R/G/0"
	utitilty = isBaseCase(state)
	if utitilty != "0":
		return utitilty
	
	value = float("inf")

	# loop in all successors/children
	for X in Successors(state):
		maxValue = MaxValue(x, Alpha, Beta)
		value = min(value, maxValue)
		if value <= Alpha:
			return value
		Beta = max(Beta, value)
	return value

# return the max value of this state
def MaxValue(state, Alpha, Beta):
	# Check if the current state is a terminal one "win/draw"
	# if yes return the utitilty "R/G/0"
	utitilty = isBaseCase(state)
	if utitilty != "0":
		return utitilty
	
	value = float("-inf")

	# loop in all successors/children
	for X in Successors(state):
		minValue = float(MinValue(X,Alpha,Beta))
		value = max(value, minValue)
		if value >= Beta:
			return value
		Alpha = max(Alpha, value)
	return value

# return action to the Interface function >> NOT DONE YET
def AlphaBeta(state):
	# Playing Logic
	no_winner = True
	turn = 0 
	while no_winner:
	    #player 1
	    if turn == 0:
	        col = int(input("choose where to play (from 0 to 6):"))

	        while col > 6 or col < 0:
	            col = int(input("choose where to play (from 0 to 6):"))

	        if column_is_full(board, col):
	            row= open_row_position(board, col)
	            drop_piece(board, row, col, "G")

	           
	    else:
	        # player 2 >> CHANGE THE 2ND PLAYER TO BOARD
	        # Tree, Alpha Beta pruning
	    	v = MaxValue(state, float("-inf"), float("inf"))
	    	
	    	# CREATE ACTION HERE
	        if column_is_full(board, col):
	            row=open_row_position(board, col)
	            drop_piece(board,row,col,"R")
	    
	    # Flip board
	    fboard = np.flip(board,0)
	    print(fboard)
	    
	    # switch turn       
	    turn = turn + 1
	    turn = turn % 2

	  



