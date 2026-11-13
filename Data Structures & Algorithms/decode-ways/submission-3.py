class Solution:
    def numDecodings(self, s: str) -> int:
        # decode string
        # 1 -26
        # top to bottom appraoch
        # dp[i] no of ways to decode up to index i
        # at each step the single accept
        # the double need to check if 10-26

        mem = {}

        def solve(i):
            #base
            if i==0 and int(s[i]) !=0:
                return 1
            if i==0 and int(s[i]) ==0:
                return 0
            if i in mem:
                return mem[i]
            if i<0:
                return 1
            
            if int(s[i])==0:
                if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                    mem[i] = solve(i-2)
                else:
                    mem[i] = 0
            else:
                if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                    mem[i] = solve(i-2) + solve(i-1)
                else:
                    mem[i] = solve(i-1)

            return mem[i]
        
        return solve(len(s)-1)