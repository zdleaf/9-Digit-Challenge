# 9 digit challenge
# Find all 9 digit numbers that satisfy the following rules
# rule 1: Each digit cannot equal it's position plus or minus 1
# rule 2: Each digit cannot be repeated i.e. must contain 1-9
# rule 3: Digits next to each other must have a difference of >= 2 eg. 1 and 4, not 1 and 3

import numpy as np

array_rule1 = np.zeros(shape=[9, 9], dtype=int) # initialise 9x9 integer array with 0's

# rule 1: Each digit cannot equal it's position plus or minus 1

# note: position 1 is first position aka, indexed by 0 in array_rule1, therefore for clarity we refer to position and possibilities as xp and yp for comparison against the rule

for x in range(0, 9): 	# position 1-9 (indexed as 0-8)
	xp = x+1 			# xp: refer to index 0 as position 1
	for y in range(0, 9): # possibilities i.e. digits 1-9
		yp = y+1		# yp: first possibility should be 1, not the index 0
		if yp != xp and yp != xp+1 and yp != xp-1:	# if possibility is possible as per rule 1
			array_rule1[x,y] = yp

print(array_rule1)

