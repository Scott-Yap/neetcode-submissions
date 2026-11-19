class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # longest increasing subsequence
        # dp(i): longest including i
        # at each pass, we do 1 + maxdp(j) j< i and nums[j] < nums[i]

        mem = {}

        def solve(i):

            if i ==0:
                return 1
            
            if i in mem:
                return mem[i]

            mp = -float('inf')

            for j in range(0,i):
                if nums[j]< nums[i]:
                    mp = max(mp, solve(j))
            
            if mp == -float('inf'):
                mp = 0
            
            mem[i] = mp + 1
            return mem[i]

        return max(solve(i) for i in range(len(nums)))