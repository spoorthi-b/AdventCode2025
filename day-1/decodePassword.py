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