# 
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        HOLD, REST, COOLDOWN = 0, 1, 2
        mem = {}
        n = len(prices)

        def solve(i, state):
            # No more trading days
            if i == n:
                return 0 if state != HOLD else float("-inf")

            if (i, state) in mem:
                return mem[(i, state)]

            if state == HOLD:
                # Keep holding OR sell today
                mem[(i, state)] = max(
                    solve(i + 1, HOLD),
                    prices[i] + solve(i + 1, COOLDOWN)
                )

            elif state == REST:
                # Skip today OR buy today
                mem[(i, state)] = max(
                    solve(i + 1, REST),
                    -prices[i] + solve(i + 1, HOLD)
                )

            else:
                # Cooldown: must skip today
                mem[(i, state)] = solve(i + 1, REST)

            return mem[(i, state)]

        # Day 0: no stock, allowed to buy
        return solve(0, REST)
