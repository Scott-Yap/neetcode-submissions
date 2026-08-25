class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for ind in range(len(nums)-1):
            for nxt in range(ind+1, len(nums)):
                if nums[ind] + nums[nxt] == target:
                    result.append(ind)
                    result.append(nxt)
        return result
            