# 9 digit challenge
# Find all 9 digit numbers that satisfy the following rules
# rule 1: Each digit cannot equal it's position plus or minus 1
# rule 2: Each digit cannot be repeated i.e. must contain 1-9
# rule 3: Digits next to each other must have a difference of >= 2 eg. 1 and 4, not 1 and 3

import numpy as np

workingArray = np.zeros(shape=[9], dtype=int) # initialise a 9 digit array to use as our working array when checking rules
workingPosition = 1 # keep track of our position in the workingArray with this int

workingArray[0] = 3 # set initial number
workingArray[workingPosition] = 5 # test

def CheckRule1(workingArray, workingPosition):
	if (workingArray[workingPosition] == workingPosition + 1 or workingArray[workingPosition] == workingPosition + 2 or workingArray[workingPosition] == workingPosition):
		return False
	else:
		return True

def CheckRule2(workingArray):
	# for each x in workingArray, keep a count of how many times the value appears, it it appears twice then rule 2 has failed
	# alternative method, take workingPos as argument and compare rest of elements to workingPos value
	countOfValues = np.zeros(shape=[9], dtype=int)
	for x in workingArray:
		if (x != 0):
			countOfValues[x - 1] += 1

	print("countOfValues: ", countOfValues)
	for y in countOfValues:
		if (y >= 2):
			return False
		else:
			return True

def CheckRule3(workingArray, workingPosition):
	# with workingPos, check pos-1 for difference of more than 2. value of pos+1 will not be filled yet so no check required
	if (workingPosition != 0):
		value1 = workingArray[workingPosition - 1]
		value2 = workingArray[workingPosition]
		difference = np.sqrt((value1-value2)*(value1-value2))
		print("difference: ", difference)
		if (difference > 2):
			return True
		else:
			return False
	else:
		return True

def CheckNextNumbers(workingArray, workingPosition):
	
	# Check we satisfied each rule
	resultRule1 = CheckRule1(workingArray, workingPosition)
	resultRule2 = CheckRule2(workingArray)
	resultRule3 = CheckRule3(workingArray, workingPosition)

	print("check Rule 1: ", resultRule1)
	print("check Rule 2: ", resultRule2)
	print("check Rule 3: ", resultRule3)

	if (resultRule1 == False or resultRule2 == False or resultRule3 == False):
		return False
	else:
		return True

evalNextNumbers = CheckNextNumbers(workingArray, workingPosition)

print("working array: ", workingArray)

print("overall evaluation: ", evalNextNumbers)

# rule 1: Each digit cannot equal it's position plus or minus 1
# note: position 1 is first position aka, indexed by 0 in array_rule1, therefore for clarity we refer to position and possibilities as xp and yp for comparison against the rule

arrayRule1 = np.zeros(shape=[9, 9], dtype=int) # initialise 9x9 integer array with 0's

for x in range(0, 9): 	# position 1-9 (indexed as 0-8)
	xp = x+1 			# xp: refer to index 0 as position 1
	for y in range(0, 9): # possibilities i.e. digits 1-9
		yp = y+1		# yp: first possibility should be 1, not the index 0
		if yp != xp and yp != xp+1 and yp != xp-1:	# if possibility is possible as per rule 1
			arrayRule1[x,y] = yp

# print(arrayRule1)

