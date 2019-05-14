import ai

def MinValue(state, Alpha, Beta):
	# Check if the current state is a terminal one "win/draw"
	# if yes return the utitilty "R/G/0"
	utitilty = isBaseCase(state)
	if utitilty != "0":
		return utitilty
	
	value = float("inf")

	# loop in all successors/children
	for X in successors(state):
		maxValue = MaxValue(x, Alpha, Beta)
		value = min(value, maxValue)
		if value <= Alpha:
			return value
		Beta = max(Beta, value)
	return value

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




# return action to the Interface function
def AlphaBeta(state):
	v = MaxValue(state, float("-inf"), float("inf"))
	return 0

#print(max(2,5))

