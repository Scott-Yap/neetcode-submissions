# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # find max maxProfit
#         # after sell, cant buy another day. cool down 
#         # own at most one at a time
#         # states:  hold, sell, rest (cool down or no buy)
#         #dp[i] max profit at the end of day i (index) 
#         # since each day has three states
#         # we track each state max everyday
#         # hold means come from buy yesterday or buy today
#         # -> rest - prices or hold 
#         # sell means hold yesterday
#         # -> hold[i-1] + prices, 
#         # rest means rest yesterday or sell yesterday
#         # -> rest[i-1] or sell[i-1]
#         hold = [0] * len(prices)
#         sell = [0] * len(prices)
#         rest = [0] * len(prices)


#         hold[0] = -prices[0]
#         sell[0] = -float('inf')
#         rest[0] = 0
#         for i in range(1,len(prices)):
            
#             #recursion
#             hold[i] = max(rest[i-1]-prices[i], hold[i-1])
#             sell[i] = hold[i-1] + prices[i]
#             rest[i] = max(rest[i-1], sell[i-1])
#         return max(sell[len(prices)-1],rest[len(prices)-1])


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # Day 0: initial states
        hold = -prices[0]
        sold = float("-inf")
        rest = 0

        for price in prices[1:]:
            new_hold = max(hold, rest - price)
            new_sold = hold + price
            new_rest = max(rest, sold)

            # Update all states together
            hold, sold, rest = new_hold, new_sold, new_rest

        return max(sold, rest)
