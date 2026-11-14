class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dont need to be adj
        # goal max length 
        # top down using mem
        # dp[i] longest length up to ind i must end at i

        mem = {}

        def solve(i):
            #base
            if i<0:
                return 0
            if i==0:
                return 1
            
            if i in mem:
                return mem[i]

            length = 0
            j = i-1
            while j >= 0:
                if nums[j] < nums[i]:
                    length = max(length, solve(j))
                j -=1
            
            mem[i] = length + 1
            return mem[i]
        
        return max([solve(i) for i in range(len(nums))])