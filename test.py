import pprint
from  ai import *
pp = pprint.PrettyPrinter()

print("***TESTING ROW***")
currentState=[['0' for col in range(7)] for row in range(6)]
currentState[5][4] = 'R'
currentState[5][1] = 'R'
currentState[5][2] = 'R'
currentState[5][3] = 'R'
pp.pprint(currentState)
print("isBaseCase:", isBaseCase(currentState))

print("***TESTING COLUMN***")
currentState=[['0' for col in range(7)] for row in range(6)]
currentState[0][1] = 'R'
currentState[1][1] = 'R'
currentState[3][1] = 'R'
currentState[2][1] = 'R'
pp.pprint(currentState)
print("isBaseCase:", isBaseCase(currentState))

print("***TESTING DIAGONAL***")
currentState=[['0' for col in range(7)] for row in range(6)]
currentState[5][0] = 'R'
currentState[4][1] = 'R'
currentState[3][2] = 'R'
currentState[2][3] = 'R'
pp.pprint(currentState)
print("isBaseCase:", isBaseCase(currentState))