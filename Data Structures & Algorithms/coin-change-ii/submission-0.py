class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # coins different denominations
        # amount target
        # number of distinct combinations that total up to amount
        # if cant return 0
        # unlimiated no of each coins
        # dp[i, s] no of distinct comb using up to ind i to s

        # each step 
        """
        [1,2,3]
        dp(i,s) = dp(i,s-coins[i]) + dp(i-1,s)

        dp(2,4) = dp(2,1) + dp(1,4)
        dp(2,1) = dp(2,-1) + dp(1,1)
        dp(1,4) = dp(1,2) + dp(0,4)
        dp(2,-1) = 0
        dp(1,1) = dp(1,-1) + dp(0,1)
        dp(1,2) = dp(1,0) + dp(0,2)
        dp(0,4) = 1
        dp(1,0) = 1
        dp(0,2) = 1
        dp(0,1) = 1
        """

        mem = {}

        def solve(i,s):
            #base
            if s<0 or i<0:
                return 0
            if s==0:
                return 1

            if (i,s) in mem:
                return mem[(i,s)]
            
            mem[(i,s)] = solve(i,s-coins[i]) + solve(i-1,s)
            return mem[(i,s)]
        
        return solve(len(coins)-1, amount)
            