## Solution Intuition:

Each move is written in the form:  L5, R42, L105, etc.

- move[0] gives the direction (L or R)
- move[1:] gives the number of dial rotations

* The dial has 100 positions (00–99).  
   Rotating 100, 200, or 400 steps always brings us back to the same position.
   Example: R105 when starting at 10:
     - 100 rotations → back to 10
     - remaining 5 rotations → end on 15
   Therefore, we can always normalize rotations as:
       rotations = rotations % 100

* Moving Right:
       curr = (curr + rotations) % 100
   If we wrap past 99 back to a smaller number (but not 0), 
   it means we completed an extra full rotation of the dial.

* Moving Left:
    ```
       curr = (curr - rotations) % 100
    ```
   If we wrap past 0 into a larger number, 
   that also indicates an additional full rotation.

* Landing exactly on 0 always counts as an extra full rotation.