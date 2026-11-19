class Solution:
    def numSquares(self, n: int) -> int:
        # recurstion: dp(i)= 1+ min(dp(i-j^2)) j< sqrtn
        from math import isqrt
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, isqrt(i) + 1):
                dp[i] = min(dp[i], 1 + dp[i - j**2])

        return dp[n]