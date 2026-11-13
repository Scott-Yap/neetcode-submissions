class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins denominations
        # amount target
        # fewest number of coins to make up target
        # if impossible -1
        # unliminated coins
        # dp(i,s) up till ind i fewest no of coins 
        # each step either want coin or dont want

        mem = {}

        def solve(i,s):
            #base
            if s==0:
                return 0
            if s<0:
                return float('inf')
            if i<0:
                return float('inf')
            
            if (i,s) in mem:
                return mem[(i,s)]
            # want and dont want
            mem[(i,s)] = min(solve(i,s-coins[i])+1, solve(i-1,s))
            return mem[(i,s)]
        
        ans = solve(len(coins) - 1, amount)
        return -1 if ans == float("inf") else ans