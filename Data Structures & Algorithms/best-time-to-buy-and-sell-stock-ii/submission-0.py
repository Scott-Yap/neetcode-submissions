class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # can buy it then sell it on the same day
        #at most one share

        profit = 0

        for i in range(1, len(prices)):
            profit += prices[i] - prices[i-1] if prices[i] > prices[i-1] else 0

        return profit