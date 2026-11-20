class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp(i) longest subseq ending at ind i 
        # at each step we check if j<i and nums[j] < nums[i]
        # that means we can increase subseq, but we the max prev

        mem = {}

        def solve(i):
            #base:
            if i==0:
                return 1
            
            # mem
            if i in mem:
                return mem[i]

            mp = 0 
            for j in range(0,i):
                if nums[j] < nums[i]:
                    mp = max(solve(j), mp)
                
            total = mp + 1
            mem[i] = total
            return total
        return max(solve(i) for i in range(0, len(nums)))