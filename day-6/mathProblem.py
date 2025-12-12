class Solution:

    def parseInput(self, inputFile):
        items = []
        with open(inputFile, 'r') as file:
            for line in file:
                values = line.replace('\n', '')
                items.append(values)
        return items
        
    def solveMathProblem(self, inputFile):
        problem = self.parseInput(inputFile)
        operators = problem[len(problem) - 1].split()
        total = 0
        curr_sub = 0 if operators[-1] == "+" else 1
        
        for col in range(len(problem[0])-1,-1,-1):
            # Parse the col to get the number
            curr_number = ""
            for row in range(len(problem) - 1):
                curr_number += problem[row][col]

            # If it is the end, update total sum, reset sub sum and update operator index
            if curr_number.strip() == "":
                total += curr_sub
                operators.pop()
                curr_sub = 0 if operators[-1] == "+" else 1
                continue

            # strip unwanted spaces
            curr_number = int(curr_number.strip())
            
            # based on operator calculate sub sum or product
            if operators[-1] == "+":
                curr_sub += curr_number
            else:
                curr_sub *= curr_number

        # consider last row's sub sum
        total += curr_sub    
        
        return total

day6Solution = Solution()
print(day6Solution.solveMathProblem("input.txt"))