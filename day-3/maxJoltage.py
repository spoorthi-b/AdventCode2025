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
    
    def totalJoltage(self, inputFile):
        banks = self.parseInput(inputFile)
        res = 0
        for bank in banks:
            res += self.maxJoltageInBank(bank)
        return res
    
    # def maxJoltageInBank(self, bank):
    #     def dfs(i,sub):
    #         if len(sub) == 12:
    #             return int(sub)
            
    #         if i >= len(bank) and len(sub) < 12:
    #             return 0

    #         return max(dfs(i+1, sub), dfs(i+1, sub + bank[i]))
    #     return dfs(0, "")
    def maxJoltageInBank(self,bank):
        n = len(bank)
        K = 12

        # dp[i][k] = best suffix (string) of length k using bank[i:]
        dp = [[""] * (K + 1) for _ in range(n + 1)]

        # Fill base cases:
        # dp[n][0] = "" ; dp[n][k>0] = invalid (None)
        for k in range(1, K+1):
            dp[n][k] = None

        # Fill DP bottom-up
        for i in range(n-1, -1, -1):
            for k in range(K + 1):
                if k == 0:
                    dp[i][k] = ""
                    continue

                # If not enough chars left, impossible
                if n - i < k:
                    dp[i][k] = None
                    continue

                # Option 1: skip this digit
                best = dp[i+1][k]

                # Option 2: take this digit
                take_suffix = dp[i+1][k-1]
                if take_suffix is not None:
                    take = bank[i] + take_suffix
                    if best is None or take > best:
                        best = take

                dp[i][k] = best

        return int(dp[0][K])

    

day3Solution = Solution()
print(day3Solution.totalJoltage("input.txt"))