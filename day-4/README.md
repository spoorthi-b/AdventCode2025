# Day 4 — Remove Paper Rolls
## Intuition:

The problem is similar to LeetCode Blind 75 problem: 200 Number of Islands.
We need to explore all paths and update the grid as we make a decision.

### DFS
Explore all paper rolls and if the paper roll can be removed, explore all
paper rolls adjecent to it.
Decisions to make at each element:
- If the element is invalid: return 0 as we are not removing anything.
- If the element cannot be replaced: return 0 as we cannot move further.
- If the element can be replaced: Remove the paper roll by changing it's grid value to "." and update the result.
 Explore all adjacent paper rolls as our move affected the outcome. When we are
 marking the paper roll as removed, we are also indirectly saying the element
 was visited.

 For in depth explanation check out NeedCode explanation: [click here](https://www.youtube.com/watch?v=pV2kpPD66nE) 