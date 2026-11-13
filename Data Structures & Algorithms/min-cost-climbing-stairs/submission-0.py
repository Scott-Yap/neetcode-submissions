class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i]= cost of taking a step from the ith floor 
        # after pay step either i+1 or i+2
        # can start either 0 or 1
        # find min cost to reach top 
        # dp[i] = min cost at that ind i
        # each step either one up or two up
        
        mem = {}

        def solve(i):
            #base 
            if i==0:
                return cost[0]

            if i < 0:
                return 0
            if i==len(cost):
                cost_ = 0
            else:
                cost_ = cost[i]
            #mem
            if i in mem:
                return mem[i]
            
            mem[i] = min(solve(i-1), solve(i-2)) + cost_

            return mem[i]
        return solve(len(cost))