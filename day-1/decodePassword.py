'''
Solution Intuition:

Each move is written in the form:  L5, R42, L105, etc.

- move[0] gives the direction (L or R)
- move[1:] gives the number of dial rotations

1. The dial has 100 positions (00–99).  
   Rotating 100, 200, or 400 steps always brings us back to the same position.
   Example: R105 when starting at 10:
     - 100 rotations → back to 10
     - remaining 5 rotations → end on 15
   Therefore, we can always normalize rotations as:
       rotations = rotations % 100

2. Moving Right:
       curr = (curr + rotations) % 100
   If we wrap past 99 back to a smaller number (but not 0), 
   it means we completed an extra full rotation of the dial.

3. Moving Left:
       curr = (curr - rotations) % 100
   If we wrap past 0 into a larger number, 
   that also indicates an additional full rotation.

4. Landing exactly on 0 always counts as an extra full rotation.

'''
class Solution:

    def parseInput(self, inputFile):
        # simple txt file parser
        input = []
        with open(inputFile, 'r') as file:
            lines = file.readlines()

        for line in lines:
            processed_line = line.strip() 
            input.append(processed_line)
        return input

    def decodePassword(self, inputFile):
        moves = self.parseInput(inputFile)
        
        # dail starts at 50
        curr = 50
        res = 0

        for move in moves:
            direction = move[0]
            val = int(move[1:])
            
            # Every full 100 adds to result
            res += val // 100
            rotations = val % 100

            # Apply rotation
            prev = curr
            if direction == "L":
                curr = (curr - rotations) % 100
                # If wrapped from >0 to 0
                if prev != 0 and curr > prev:
                    res += 1
            else:  # "R"
                curr = (curr + rotations) % 100
                # If wrapped from <99 to something small but not zero
                if curr < prev and curr != 0:
                    res += 1

            # Extra count if landing on 0
            if curr == 0:
                res += 1
        return res

day1Solution = Solution()
print(day1Solution.decodePassword("input.txt"))