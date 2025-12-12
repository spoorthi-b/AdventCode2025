# Day 6 — Solve Math Problem
### Intuition

The challenge is to:
- Read numbers column by column, starting from the rightmost column.
- Detect where a column ends (i.e., a vertical separator where all characters are spaces).
- For each block of columns:
    - Combine the digits to form numbers.
    - Apply the corresponding operator (+ or *) across all numbers in that block.
- Add the results of each block to a final total.

#### Approach
1. Extract operators: The last row of the input contains operators:
```
    operators = problem[last_row].split()
```
current operator will always be the last element

2. Process columns from right → left
- Parse the current column and get the number by appending each row character
- Check if the column makrs an end
- If column does not mark the end:
    - update your current sub, based on the current operator
- If column marks the end:
    - add the current sub to the total
    - pop the last element in the operators array
    - reset the current sub to 0 if the current operator is + else to 1


Time Complexity: O(mxn)