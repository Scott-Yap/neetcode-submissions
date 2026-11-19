class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums i amout of i has
        # straight line 
        # cant rob adacent ones
        # max amount 
        # dp(i): max up to house i. each step either robbed i-1 or robbed i-2 (row here)
        # base: i<0: 0 
        # need array then just do top bottom

        mem = {}

        def solve(i):

            if i<0:
                return 0
            
            if i in mem:
                return mem[i]
            
            mem[i] = max(solve(i-2)+ nums[i], solve(i-1) )

            return mem[i]
        
        return solve(len(nums)-1)

