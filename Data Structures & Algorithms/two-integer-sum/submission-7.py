class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()

        for ind in range(len(nums)):
            if nums[ind] in diff:
                return [diff[nums[ind]], ind]

            diff[target-nums[ind]] = ind

