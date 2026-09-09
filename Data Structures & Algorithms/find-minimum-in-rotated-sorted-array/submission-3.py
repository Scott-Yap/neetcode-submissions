class Solution:
    def findMin(self, nums: List[int]) -> int:
        # do binary search for Olog(n)

        mid = round(len(nums) / 2)
        left = 0
        right = len(nums) - 1

        while left < right:
            
            if nums[mid] > nums[right]:
                left = mid + 1
                mid = round((right - left) / 2) + left
            else:
                right = mid
                mid = round((right - left) / 2) + left
        
        return nums[left]





        