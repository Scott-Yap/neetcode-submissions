class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums find largest subarry sum 
        # dp(i)= largest subarray sum up including i
        # at each step we either extend the subarray or we start the subarray at i
        # [2,-3,4]
        # solve(2) = max(solve(1)+nums[i], nums[i])
        # base i==0: return nums[0] if <0; return 0

        #try bottom up

        current = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            current = max(current+nums[i], nums[i])
            best = max(best, current)

        return best

            