class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top down 
        # dp(i,s): up to i ind fewest number to make up target s
        # base: i<0 return 0, s<0 -> -1
        # each step either take i or not take i
        # [2] a = 3

        mem = {}

        def solve(i,s):

            #base
            if s==0:
                return 0
            if s<0 or i<0:
                return float('inf')
            
            if (i,s) in mem:
                return mem[(i,s)]
            
            mem[(i,s)] = min(solve(i-1,s), 1+solve(i,s-coins[i]))

            return mem[(i,s)]
        
        result = solve(len(coins)-1, amount) 

        if result == float('inf'):
            return -1
        else:
            return result