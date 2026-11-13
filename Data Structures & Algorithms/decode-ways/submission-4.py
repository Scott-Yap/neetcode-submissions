class Solution:
    def numDecodings(self, s: str) -> int:
        # decode string
        # 1 -26
        # top to bottom appraoch
        # dp[i] no of ways to decode up to index i
        # at each step the single accept
        # the double need to check if 10-26

        # mem = {}

        # def solve(i):
        #     #base
        #     if i==0 and int(s[i]) !=0:
        #         return 1
        #     if i==0 and int(s[i]) ==0:
        #         return 0
        #     if i in mem:
        #         return mem[i]
        #     if i<0:
        #         return 1
            
        #     if int(s[i])==0:
        #         if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
        #             mem[i] = solve(i-2)
        #         else:
        #             mem[i] = 0
        #     else:
        #         if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
        #             mem[i] = solve(i-2) + solve(i-1)
        #         else:
        #             mem[i] = solve(i-1)

        #     return mem[i]
        
        # return solve(len(s)-1)

        memo = {}

        def solve(i):
            # Empty prefix: one valid way to finish decoding
            if i < 0:
                return 1

            # A leading zero cannot be decoded
            if i == 0:
                return 0 if s[0] == "0" else 1

            if i in memo:
                return memo[i]

            ways = 0

            # Option 1: Decode the final digit
            if s[i] != "0":
                ways += solve(i - 1)

            # Option 2: Decode the final two digits together
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                ways += solve(i - 2)

            memo[i] = ways
            return ways

        return solve(len(s) - 1)
