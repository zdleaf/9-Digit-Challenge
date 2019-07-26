# 9 digit challenge
# Find all 9 digit numbers that satisfy the following rules
# rule 1: Each digit cannot equal it's position plus or minus 1 (array[0] is position 1)
# rule 2: Each digit cannot be repeated i.e. must contain 1-9
# rule 3: Digits next to each other must have a difference of >= 3 e.g. 1 and 4, not 1 and 3

import numpy as np
import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# uncomment to show logging/calculation

def CheckRule1(workingArray, workingPosition):
	# check value doesn't equal it's position +1 or -1
	if (workingArray[workingPosition] == workingPosition + 1 or workingArray[workingPosition] == workingPosition + 2 or workingArray[workingPosition] == workingPosition):
		return False
	else:
		return True

def CheckRule2(workingArray):
	# for each x in workingArray, keep a count of how many times the value appears, it it appears twice then rule 2 has failed
	# alternative/potentially faster method, take workingPos as argument and compare elements that come before
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
	# with workingPos, check pos-1 for difference of more than 2
	# since we're building numbers left to right one digit at a time, value of pos+1 will not be filled yet so no check required
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
	# check we satisfied each rule
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

def CalculatePotentials(workingArray, workingPosition):
	potentialsArray = []
	for x in range(1, 10):
		workingArray[workingPosition] = x
		if (CheckRules(workingArray, workingPosition) == True): # if x satisfies all rules
			potentialsArray.append(x)
		logging.debug("workingArray: %r", workingArray)
	return potentialsArray

def MergeNewPotentials(runningList, newPotentials):
	# merge an old runningList with a list of new potentials
	newList = []
	for index, value in enumerate(runningList):
		for y in newPotentials[index]: # index in runningList and newPotentials correspond, e.g. newPotentials[1] is possibilities for runningList[1] etc.
			newList.append(int(str(value) + str(y)))
	return newList

def CreateWorkingArray(intValue):
	# we need to pass CalculatePotentials() a 9 digit array, create this from a given number e.g. 361 --> [3, 6, 1, 0, 0, 0, 0, 0, 0]
	split = [int(d) for d in str(intValue)] 
	workingArray = np.zeros(shape=[9], dtype=int)
	for index, value in enumerate(split):
		workingArray[index] = value
	return workingArray

runningList = [0]

for position in range(0,9):
	potentialValues = [] # clear values each loop
	for x in runningList:
		workingArray = CreateWorkingArray(x) # build a 9 digit array from x
		potentialValues.append(CalculatePotentials(workingArray, position)) # calculate the next potential values in given position and append to an array

	runningList = MergeNewPotentials(runningList, potentialValues) # merge the values into a new list ready for next loop

	logging.info("potentialValues (%r): %r", len(potentialValues), potentialValues)
	logging.info("runningList (%r): %r", len(runningList), runningList)

print(runningList)
