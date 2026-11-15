class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # top left, go to bottom right
        # only down or right 
        # obstacle marked as 1 
        # return no of possible unique paths
        # dp(i,j) no of possible paths to i,j
        # each step right or down
        # we skip if obstacle, 
        # base: first column, first row, =1 if no obstacle

        mem = {}

        def solve(i,j):

            #base 
            if i<0 or j<0:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1

            if (i,j) in mem:
                return mem[(i,j)]
            
            mem[(i,j)] = solve(i, j-1) + solve(i-1, j)
            return mem[(i,j)]
        
        return solve(len(obstacleGrid)-1,len(obstacleGrid[0])-1)