class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # roll n times
        # faces from 1-k
        # count outcomes faces sum to target
        # return count modulo 1000000007
        # if cant return 0

        # recursion new roll: we go through 1-k and track the target
        # dp(i,s) i = no of roll, s = target. no of ways 
        # top down so we want to do roll 1 first then all the way down 

        m = 10**9+7
        mem = {}

        def solve(i,s):
            # base: 
            if i==n and s==0:
                return 1  
            if i==n: 
                return 0

            if s < 0:
                return 0

            if (i,s) in mem:
                return mem[(i,s)]
            ways = 0
            for val in range(1,k+1):
                ways += solve(i+1,s-val)
            mem[(i,s)] = ways%m
            return ways%m
        return solve(0, target)