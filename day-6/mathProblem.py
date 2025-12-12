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
        last_row = len(problem) - 1
        operators = problem[last_row].split()
        operators_index = len(operators) - 1
        total = 0
        curr_sub = 0 if operators[operators_index] == "+" else 1
        
        for col in range(len(problem[0])-1,-1,-1):
            # Check if the current col is the end
            endOfCol = True
            for row in range(last_row):
                if problem[row][col] != " ":
                    endOfCol = False
                    break

            # If it is the end, update total sum, reset sub sum and update operator index
            if endOfCol:
                total += curr_sub
                operators_index -= 1
                curr_sub = 0 if operators[operators_index] == "+" else 1
                continue

            # Parse the col to get the number
            curr_number = ""
            for row in range(last_row):
                curr_number += problem[row][col]

            # strip unwanted spaces
            curr_number = int(curr_number.strip())
            
            # based on operator calculate sub sum or product
            if operators[operators_index] == "+":
                curr_sub += curr_number
            else:
                curr_sub *= curr_number

        # consider last row's sub sum
        total += curr_sub    
        
        return total + curr_sub

day6Solution = Solution()
print(day6Solution.solveMathProblem("input.txt"))
