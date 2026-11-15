class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums[i] max length canJump
        # true if can reach last index, else false
        # [1,2,0,1,0] 0->1->4-> 5 return true
        #can do bottom up acutally
        # keep track of furthest reach
        # each step check if can reach me or further or cant

        current = 0 + nums[0]
        best = 0 + nums[0]

        for i in range(1, len(nums)):
            if current >= i: 
                current = max(current, i + nums[i])
            best = max(current, best)
        
        return best >= len(nums)-1
