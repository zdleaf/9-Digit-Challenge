
# 9 Digit Challenge

The 9 Digit Challenge is to find all 9 digit numbers that satisfy the following rules:

 1. **Each digit cannot equal it's position plus or minus 1 (position is 1-9, i.e. not 0 indexed) ** 
 2. **Each digit cannot be repeated i.e. must contain integers 1-9**
 3. **Digits next to each other must have a difference of >= 3 e.g. 1 and 4, not 1 and 3**

For example, 385174926.


This solution builds every possibility, starting from the left hand side. We start with a 9 digit array of zeros [0, 0, 0, 0, 0, 0, 0, 0, 0] and start calculating at array[0]. 

We test at the first position where x is 1-9: [x, 0, 0, 0, 0, 0, 0, 0, 0]. For example, [1, 0, 0, 0, 0, 0, 0, 0, 0] which fails under rule 1.

This produces the following possibilities for the first position: **[3, 4, 5, 6, 7, 8, 9]**

For each value in this list we then determine the next potential numbers at position 2. For example, for 3 in the first position, the only numbers that satisfy all rules in position 2 are 6, 7, 8, 9.

The list of potentials is stored in a list of lists as below:

2019-02-10 16:41:37,998 - INFO - potentialValues: **[[6, 7, 8, 9], [7, 8, 9], [8, 9], [9], [4], [4, 5], [4, 5, 6]]**

We can then merge this with the values from before to get a running list of all numbers:

2019-02-10 16:41:37,998 - INFO - runningList: **[36, 37, 38, 39, 47, 48, 49, 58, 59, 69, 74, 84, 85, 94, 95, 96]**

We continue this process, looping until we get to 9 digits and the full list of numbers:

**[385174926, 385174962, 385274916, 385274961, 471839526, 471938526, 481639527, 481739526, 485172936, 485172963, 485173926, 485173962, 485271936, 485271963, 485273916, 485273961, 491638527, 491738526, 741839526, 741938526, 749638152, 749638251, 841639527, 841739526, 859274163, 941638527, 941738526, 958274163]**
