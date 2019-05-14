import ai

def MinValue(state, Alpha, Beta):
	if isBaseCase(state) != "0":
		value = "PosInf"
def MaxValue(state, Alpha, Beta):
	# Check if the current state is a terminal one "win/draw"
	# if yes return the utitilty "R/G/0"
	if isBaseCase(state) != "0":
		return 
	# Put value to negative infinity
	value = "NegInf"

	# loop in all successors/children
	for X in Successors(state):
		value = max(value, MinValue(X,Alpha,Beta))
		if value >= Beta:
			return value
		Alpha = max(Alpha, value)
	return value




# return action to the Interface function
def AlphaBeta(state):
	v = MaxValue(state, "NegInf", "PosInf")
	return 0

#print(max(2,5))

