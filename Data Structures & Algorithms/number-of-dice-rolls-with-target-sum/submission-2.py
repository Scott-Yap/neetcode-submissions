class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # think of it in trees
        # each roll has 1 -k possibilityes
        # then next roll same thing, and we just have to keep track, until reach target = 0 if not not valid
        # n number of times rolling, target we track. 
        # each recursion, we look at all possible values 
        # dp(i,s): ith roll the target we going for
        # = res + dp(i-1, s-j) for j in 1 to k
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