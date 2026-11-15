class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low sell high
        # track max profit can do O(n)
        # if next is lower then treat it as buy and keep track of profit every day after higher

        maxp = 0
        current = prices[0]
        for i in range(1,len(prices)):

            #check if bigger:
            if prices[i] > current:
                maxp = max(maxp, prices[i]-current)
            else:
                current = prices[i]
        
        return maxp