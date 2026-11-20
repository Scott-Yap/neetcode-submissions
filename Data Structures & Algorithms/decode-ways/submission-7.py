class Solution:
    def numDecodings(self, s: str) -> int:
        # decoding the strings
        # for unit digit: 1-9
        # for double digit: 10-26
        # top down
        # no ways up to i

        mem = {}

        def solve(i):
            # base 
            if i<0:
                return 1
            if i==0 and int(s[0])!=0:
                return 1
            if i==0:
                return 0

            if i in mem:
                return mem[i]
            
            ways = 0
            # unit digit first
            if 1 <= int(s[i]) <= 9:
                ways += solve(i-1)
            
            if 10 <= int(s[i-1:i+1]) <= 26:
                ways += solve(i-2)
            
            mem[i] = ways
            return ways
        
        return solve(len(s)-1)
