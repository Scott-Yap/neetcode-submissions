class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # now inlcuding cost and we want min cost
        # can do bottom up
        # dp(i) = min(dp(i-1), dp(i-2)) + cost[i]
        # base dp0 = cost[0], dp1 = cost[1]

        d0 = cost[0]
        d1 = cost[1]

        for i in range(2, len(cost)):
            new = min(d1, d0) + cost[i]
            d0 = d1
            d1 = new
        
        return min(d1,d0)