class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i]: amount of money
        # straight line
        # cant rob two adj houses
        # max amount
        # dp[i] max amount at ind i
        # each stage can either rob i or not rob i

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