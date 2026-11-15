class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums find largest subarry sum 
        # dp(i)= largest subarray sum up including i
        # at each step we either extend the subarray or we start the subarray at i
        # [2,-3,4]
        # solve(2) = max(solve(1)+nums[i], nums[i])
        # base i==0: return nums[0] if <0; return 0

        mem ={}

        def solve(i):
            if i<0:
                return 0
            if i==0:
                return nums[i]
            if i in mem:
                return mem[i]

            mem[i] = max(solve(i-1)+nums[i], nums[i])
            return mem[i]
        
        return max(solve(i) for i in range(len(nums)))