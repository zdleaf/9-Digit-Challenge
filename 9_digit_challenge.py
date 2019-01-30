# 9 digit challenge
# Find all 9 digit numbers that satisfy the following rules
# rule 1: Each digit cannot equal it's position plus or minus 1 (array[0] is position 1)
# rule 2: Each digit cannot be repeated i.e. must contain 1-9
# rule 3: Digits next to each other must have a difference of >= 2 eg. 1 and 4, not 1 and 3

import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') #

# workingArray[0] = 1 # set initial number
# workingArray[workingPosition] = 6 # test

def CheckRule1(workingArray, workingPosition):
	if (workingArray[workingPosition] == workingPosition + 1 or workingArray[workingPosition] == workingPosition + 2 or workingArray[workingPosition] == workingPosition):
		return False
	else:
		return True

def CheckRule2(workingArray):
	# for each x in workingArray, keep a count of how many times the value appears, it it appears twice then rule 2 has failed
	# alternative method, take workingPos as argument and compare rest of elements to workingPos value e.g. until workingPos = 0, keep workingPos - 1 and compare
	countOfValues = np.zeros(shape=[9], dtype=int)
	for x in workingArray:
		if (x != 0):
			countOfValues[x - 1] += 1

	logging.debug("countOfValues: %r", countOfValues)
	if any(y >= 2 for y in countOfValues):
		return False
	else:
		return True

def CheckRule3(workingArray, workingPosition):
	# with workingPos, check pos-1 for difference of more than 2. value of pos+1 will not be filled yet so no check required
	if (workingPosition != 0):
		value1 = workingArray[workingPosition - 1]
		value2 = workingArray[workingPosition]
		difference = np.sqrt((value1-value2)*(value1-value2)) # square and sqrt to always provide positive difference
		logging.debug("difference: %r", difference)
		if (difference > 2):
			return True
		else:
			return False
	else:
		return True

def CheckRules(workingArray, workingPosition):
	
	# Check we satisfied each rule
	resultRule1 = CheckRule1(workingArray, workingPosition)
	resultRule2 = CheckRule2(workingArray)
	resultRule3 = CheckRule3(workingArray, workingPosition)

	logging.debug("check Rule 1: %r", resultRule1)
	logging.debug("check Rule 2: %r", resultRule2)
	logging.debug("check Rule 3: %r", resultRule3)

	if (resultRule1 == False or resultRule2 == False or resultRule3 == False):
		return False
	else:
		return True

## function calculate potentials, returns array of potentials
def CalculatePotentials(workingArray, workingPosition): # optionsArray, calcPosition
	y = 0
	temporaryPotentials = []
	for x in range(1, 10):
		workingArray[workingPosition] = x
		if (CheckRules(workingArray, workingPosition) == True): # if x satisfies rules
			temporaryPotentials.append(x) # add to an array
			y += 1 # move the next position in the array
		print("workingArray: ", workingArray)
		print("----------")
	return temporaryPotentials

# first round, calculating first position
calcPosition = 0 # what position are we generating? need to keep track of this for general
workingArray = np.zeros(shape=[9], dtype=int) # initialise a 9 digit array to use as our working array when checking rules
workingPosition = 0 # keep track of our position in the workingArray with this int
potentials = []
potentials = CalculatePotentials(workingArray, workingPosition)
print("potentials 1: ", potentials)
print("----------")
workingArray[calcPosition] = potentials[0] # set position 0 to first potential
workingPosition = 1
potentials = CalculatePotentials(workingArray, workingPosition)
print("potentials 2: ", potentials)

# need to loop all and tree this off 
# for x in potentials
# CalculatePotentials(x)

print("----------")
print("calcPosition: ", calcPosition)
# print("working array: ", workingArray)
# print("temp potentials: ", temporaryPotentials)







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

