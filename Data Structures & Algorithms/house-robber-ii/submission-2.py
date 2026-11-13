class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i]: amount
        # arranged in circles
        # no two adj
        # max amount
        # [3,4,3]
        # solve 0 = 3, solve 1 = 4, solve 2 = 4 separate check for final 
        if len(nums) == 1:
                return nums[0]
        def rob_1(nums: List[int]) -> int:
            # nums[i]: amount of money
            # straight line
            # cant rob two adj houses
            # max amount
            # dp[i] max amount at ind i
            # each stage can either rob i or not rob i
            if len(nums) == 1:
                return nums[0]
            mem = {}
            def solve(i):
                if i<0:
                    return 0
                if i==0:
                    return nums[0]
                
                #mem
                if i in mem:
                    return mem[i]
                
                # recursion
                mem[i] = max(solve(i-2)+nums[i], solve(i-1))

                return mem[i]
            return solve(len(nums)-1)
        
        return max(rob_1(nums[1:]), rob_1(nums[:-1]))