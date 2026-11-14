class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # nums, target
        # either add or subtract
        # dp(i,s) no of ways up to ind i
        # add: dp(i-1,s-nums[i])
        # sub: dp(i-1, s+nums[i])
        # [2,2,2]
        # dp(2,2) = dp(1,0) + dp (1,4)
        # dp(1,0) = dp(0,-2) + dp(0,2)
        # dp(1,4) = dp(0,2) + dp(0,6)
        # dp(0,-2) = 1
        # dp(0,2) = 1
        # works
        # base i==0 depends on last digit

        mem = {}
        def solve(i,s):
            if i == 0:
                return int(s == nums[0]) + int(s == -nums[0])
            
            if (i,s) in mem:
                return mem[(i,s)]
            
            mem[(i,s)] = solve(i-1, s-nums[i]) + solve(i-1, s+nums[i])
            return mem[(i,s)]
        return solve(len(nums)-1, target)