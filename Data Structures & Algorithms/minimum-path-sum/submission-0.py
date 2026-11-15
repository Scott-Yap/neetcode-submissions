class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # mxn grid
        # find the minimum minPathSum
        # each point has a weight
        # can go down or right
        # dp[i,j] min sum of path to i,j
        # base grid[0][0] at start

        mem = {}

        def solve(i,j):
            #base
            if i<0 or j<0:
                return float('inf')
            if i==0 and j==0:
                return grid[0][0]
            if (i,j) in mem:
                return mem[(i,j)]
            mem[(i,j)] = min(solve(i-1,j), solve(i,j-1))+grid[i][j]
            return mem[(i,j)]
        
        return solve(len(grid)-1, len(grid[0])-1)