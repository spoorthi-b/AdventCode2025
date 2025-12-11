# Day 3 — Maximum Joltage
## Intuition
### DFS
Explore two paths at every index:
1. Maximum number if the value at index i is accepted
2. Maximum number if the value at index i is not accepted

Time Complexity = O(m x 2^n)

This worked for a small input but for a large input it was
taking too long

### Dynamic Programming, Bottom up approach
Have a 2 matrix of shape (n x k), n = length of bank + 1, k = 13
We have extra row and column as a buffer so, we do not run not in range error

Start working from bottom up as in from the last index in the bank
There are three choices at each index
- When index is invalid: n - i < k, There are not enough characters trailing 
the current index to be considered a valid joltage
- Edges: k = 0, There is no valid input 
- When Index is valid: We need to consider two choices:
    1. The value at current index is included, our string would be
        ```
            dp[i][k] = bank[i] + dp[i+1][k-1]
        ```
    2. The value at current index is not included, our strind would be
        ```
            dp[i][k] = dp[i+1][k]
        ```
Pick the maximum out of these two choices.
Keep making these three choice till we reach dp[0][12], which would be our answer

Time Complexity = O(m x n)