class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # partition two subet, the sum equal
        # means total has to be even
        # then we focus on hitting the half total on one subset 
        # at each step take or not take the nums
        # output is bool
        # dp(i,s) able to make target s at ind i 
        
        mem = {}
        total = sum(nums)
        if total%2!=0:
            return False
        target = total//2

        def solve(i,s):
            #base
            if s==0:
                return True
            if i<0:
                return False
            
            if (i,s) in mem:
                return mem[(i,s)]

            mem[(i,s)] = solve(i-1,s) or solve(i-1,s-nums[i])

            return mem[(i,s)]
        
        return solve(len(nums)-1, target)