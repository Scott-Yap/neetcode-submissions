class Solution:
    def climbStairs(self, n: int) -> int:
        # n: no of steps to reach top
        # each step 1 or 2 stpes
        # no of distinct way
        # dp top to bottom
        # dp[i] no of distinct way to ind i
        # dp[i] = dp[i-1] + dp[i-2]
        
        mem = {}

        def solve(i):
            #base
            if i==0:
                return 1
            if i<0:
                return 0
            #mem
            if i in mem:
                return mem[i]
            #rec
            mem[i] = solve(i-1) + solve(i-2)
            return mem[i]
        
        return solve(n)