class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # find no of paths have Obstacles
        # dp(i,j) no of paths to i,j 
        # if got 1 then can't take the paths
        # top down with mem

        # base 0,0 = 1, i<0 or j<0 = 0

        mem = {}

        def solve(i,j):

            if obstacleGrid[i][j] == 1:
                return 0
                
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0

            

            if (i,j) in mem:
                return mem[(i,j)]
            
            mem[(i,j)] = solve(i-1,j) + solve(i,j-1)

            return mem[(i,j)]

        
        return solve(len(obstacleGrid)-1, len(obstacleGrid[0])-1)