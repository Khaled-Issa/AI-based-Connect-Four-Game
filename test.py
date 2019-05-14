import pprint
from  ai import *


# make rows and cols equal
def equal(rows, cols):
	if len(rows) < len(cols):
		for i in range(len(cols)-1):
			rows.append(rows[0])
	elif len(rows) > len(cols):
		for i in range(len(rows)-1):
			cols.append(cols[0])
	return rows, cols
def test(rows, cols):
	pp = pprint.PrettyPrinter()
	currentState=[['0' for col in range(7)] for row in range(6)]
	# make rows and cols equal
	rows, cols = equal(rows, cols)
	for i in range(len(rows)):
		currentState[rows[i]][cols[i]] = 'R'
	pp.pprint(currentState)
	try: 
		print("isBaseCase:", isBaseCase(currentState))
	except:
		print("Test failed")


print("***TESTING ROW***")
test([0], [1,2,3,4])

print("***TESTING COLUMN***")
test([0,1,3,2], [1])

print("***TESTING DIAGONAL***")
test([5,4,3,2], [0,1,2,3])

