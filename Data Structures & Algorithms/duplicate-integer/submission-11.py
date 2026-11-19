class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = set()

        for i in nums:
            if i in exist:
                return True
            exist.add(i)
        return False