class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        M = 1000000007

        mem = {}

        def solve(i, s):
            #base
            if i==0:
                return 1 if s==0 else 0
            
            if (i,s) in mem:
                return mem[(i,s)]
            res = 0
            for j in range(1,k+1):
                res += solve(i-1, s-j)
            
            mem[(i,s)] = res%M
            return mem[(i,s)]
        
        return solve(n, target)