class Solution:
    def jump(self, nums: List[int]) -> int:
        # min number of jumps to reach the last position
        # always have a valid answer
        # use dp top bottom with mem
        # dp(i) min no jumps to reach i or above i
        # [2,4,1]
        # dp(2) = dp(j)+1 if nums[j] +j goes to i or above
        # base
        # dp(0) = 1

        mem = {}

        def solve(i):
            if i==0:
                return 0
            
            if i in mem:
                return mem[i]

            minimum = float('inf')
            for j in range(0, i):
                if nums[j] + j >= i:
                    minimum = min(minimum, solve(j)+1)
            mem[i] = minimum
            return mem[i]
        
        return solve(len(nums)-1)