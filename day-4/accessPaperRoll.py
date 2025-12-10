class Solution:

    def parseInput(self, inputFile):
        with open(inputFile, 'r') as f:
            return [list(line.strip()) for line in f]

    def canRoleBeRemoved(self, grid, r, c):
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        # check 8 adjacent value
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    count += 1
        return count < 4

    def numberOfAccessibleRolls(self, inputFile):
        grid = self.parseInput(inputFile)
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "@":
                return 0
            if not self.canRoleBeRemoved(grid, r, c):
                return 0
            
            # mark as visited
            grid[r][c] = "."
            count = 1
            
            # explore 8 adjacent node
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr != 0 or dc != 0:
                        count += dfs(r + dr, c + dc)
            return count

        total = 0
        for r in range(rows):
            for c in range(cols):
                total += dfs(r, c)
        return total

    
day4Solution = Solution()
print(day4Solution.numberOfAccessibleRolls("input.txt"))