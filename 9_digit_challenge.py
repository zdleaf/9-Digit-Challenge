# 9 digit challenge
# Find all 9 digit numbers that satisfy the following rules
# rule 1: Each digit cannot equal it's position plus or minus 1 (array[0] is position 1)
# rule 2: Each digit cannot be repeated i.e. must contain 1-9
# rule 3: Digits next to each other must have a difference of >= 2 eg. 1 and 4, not 1 and 3

import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

def CalculatePotentials(workingArray, workingPosition):
	potentialsArray = []
	for x in range(1, 10):
		workingArray[workingPosition] = x
		if (CheckRules(workingArray, workingPosition) == True): # if x satisfies all rules
			potentialsArray.append(x)
		logging.debug("workingArray: %r", workingArray)
	return potentialsArray

def CreateRunningList(runningList, newPotentials):
	newList = []
	for index, value in enumerate(runningList):
		for y in newPotentials[index]: # index in runningList and newPotentials correspond, i.e. newPotentials[1] is possibilities for runningList[1] etc.
			newList.append(int(str(value) + str(y)))
	return newList

# first round, calculating first position
calcPosition = 0 # what position are we generating? need to keep track of this for general
workingArray = np.zeros(shape=[9], dtype=int) # initialise a 9 digit array to use as our working array when checking rules
workingPosition = 0 # keep track of our position in the workingArray with this int

levelOne = CalculatePotentials(workingArray, workingPosition)
print("levelOne: ", levelOne)
print("----------")

# second position
levelTwo = []
for x in levelOne:
	workingArray[calcPosition] = x # set position 0 to first potential
	workingPosition = 1
	levelTwo.append(CalculatePotentials(workingArray, workingPosition))
	# print("calculating for {}, potentials: {}".format(x, potentials))
	
runningList = CreateRunningList(levelOne, levelTwo)

levelThree = []
for x in runningList:
	# runningList to workingArray function?
	split = [int(d) for d in str(x)]
	# logging.info("split: %r", split)
	for index, value in enumerate(split):
		workingArray[index] = value
	# logging.info("wA: %r", workingArray)	
	workingPosition = 2
	levelThree.append(CalculatePotentials(workingArray, workingPosition))

runningList2 = CreateRunningList(runningList, levelThree)

# iterate through the running list putting it into workingArrays and get 3rd potentials?
# function to generate new possibilities from running list
# function to generate running list from previous list, and new possibilities

print("levelTwo potentials: ", levelTwo)
print("runningList: ", runningList)	
print("levelThree potentials: ", levelThree)
print("runningList2: ", runningList2)	

print("----------")

