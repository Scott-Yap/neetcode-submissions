class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down approach
        # dp(i,j) ways to reach i,j
        # at each step either right or down

        mem = {}

        def solve(i,j):
            #base
            # first row and first column on have one ways
            if i==0 or j==0:
                return 1
            
            if (i,j) in mem:
                return mem[(i,j)]

            #recursion
            # to reach i,j we come from (i,j-1) or (i-1,j)
            mem[(i,j)] = solve(i,j-1) + solve(i-1,j)
            return mem[(i,j)]

        return solve(m-1,n-1)
