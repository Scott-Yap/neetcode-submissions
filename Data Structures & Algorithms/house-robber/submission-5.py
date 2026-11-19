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

            can_rob = 0

            for j in range(0,i-1):
                can_rob = max(can_rob, solve(j))
            
            mem[i] = max(can_rob + nums[i], solve(i-1) )

            return mem[i]
        
        return solve(len(nums)-1)

