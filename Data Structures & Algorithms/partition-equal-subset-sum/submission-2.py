class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # want equal two subset
        # need total to be even
        #then target is just half of it 
        # then we see if the nums can hit 
        # dp(i,s) = up to ind i can hit target s
        # each step can include or dont need i 
        # [1,1] solve(1, 1) = solve(0,0) or solve(0,1)

        mem = {}

        total = sum(nums)
        if total%2!=0:
            return False
        target = total//2

        def solve(i,s):
            #base
            if s == 0:
                return True

            if i < 0 or s < 0:
                return False

            #mem
            if (i,s) in mem:
                return mem[(i,s)]
            
            mem[(i,s)] = solve(i-1,s-nums[i]) or solve(i-1,s)

            return mem[(i,s)]
        
        return solve(len(nums)-1, target)