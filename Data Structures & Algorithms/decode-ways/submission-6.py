class Solution:
    def numDecodings(self, s: str) -> int:
        # no of ways to decode the string
        # top down approach with mem
        # at each step need to consider the adding digit and the last two digit
        # requirement: single (1-9), double (10-26)
        # dp(i): no of ways to decode up to ind i

        mem = {}

        def solve(i):
            if i < 0:
                return 1

            if i in mem:
                return mem[i]

            ways = 0

            # Decode one digit
            if s[i] != "0":
                ways += solve(i - 1)

            # Decode two digits
            if i >= 1 and 10 <= int(s[i-1:i+1]) <= 26:
                ways += solve(i - 2)

            mem[i] = ways
            return ways

        return solve(len(s) - 1)