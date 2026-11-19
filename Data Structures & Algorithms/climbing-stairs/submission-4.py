class Solution:
    def climbStairs(self, n: int) -> int:
        # distinct ways
        # each step either 1 or 2
        # recursion dp(i) = dp(i-1) + dp(i-2)

        d0 = 1
        d1 = 1

        for i in range(2, n+1):
            new = d1 + d0
            d0 = d1
            d1 = new

        return d1