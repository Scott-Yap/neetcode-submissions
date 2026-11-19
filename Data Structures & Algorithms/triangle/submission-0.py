class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # top bottom
        # recursion: current val + min(dp(row+1,col), dp(row+1,col+1))

        mem = {}

        def solve(i,j):
            if i>= len(triangle):
                return 0

            if (i,j) in mem:
                return mem[(i,j)]
            
            mem[(i,j)] = triangle[i][j] + min(solve(i+1,j), solve(i+1, j+1))

            return mem[(i,j)]
        
        return solve(0,0)