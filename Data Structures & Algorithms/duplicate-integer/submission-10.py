class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set(nums)

        return len(nums) != len(unique_set)