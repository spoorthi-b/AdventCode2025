# Day 2 — Find Invalid IDs
## Intuition:

We need to identify numbers that are formed by repeating a smaller
substring (pattern) x at least n times, where n ≥ 2.

Examples:
- 11111    → x = "1",   n = 5
- 121212   → x = "12",  n = 3
- 123123   → x = "123", n = 2

### Approach:
Convert the number to a string and check whether there exists a 
substring (pattern) such that:
```
    pattern * n == number   (with n ≥ 2)
```

Pattern Length Limits:
Since n ≥ 2, the pattern can be at most half the length of the number.

For numbers of length L:
- If L is even: max pattern length = L // 2
- If L is odd:  max pattern length = (L // 2) + 1

Therefore, the maximum possible pattern length is:
```
    (len(number) // 2) + 1
```