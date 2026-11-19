class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # from top left to bottom right
        # min the sum ofonumbers alogn the way
        # each move right or down
        # dp(i,j) = min right dp(i,j-1), down dp(i-1,j) + grid[i][j]
        # base 0,0 =grid[0][0] if any neg = 0
        # try bottom up

        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]    

        #base 
        dp[0][0] = grid[0][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
    
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        return dp[-1][-1]