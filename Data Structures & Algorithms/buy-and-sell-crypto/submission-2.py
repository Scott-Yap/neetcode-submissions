class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # price at each day
        # max maxProfit
        # one day to buy different day to sell
        minp = float('inf')
        maxp = -float('inf')

        for i in prices:
            minp = min(minp, i)
            maxp = max(maxp, i-minp)
        return maxp