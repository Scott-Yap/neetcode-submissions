class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min_ind = 0

        maxp = 0
        min_start = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_start:
                min_start = prices[i]
            else:
                maxp = max(maxp, prices[i] - min_start)

        return maxp
