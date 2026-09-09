class Solution:
    def findMin(self, nums: List[int]) -> int:
        # do binary search for Olog(n)

        mid = len(nums) // 2
        left = 0
        right = len(nums) - 1

        while left < right:
            
            if nums[mid] > nums[right]:
                left = mid + 1
                mid = left + (right - left) // 2
            else:
                right = mid
                mid = left + (right - left) // 2
        
        return nums[left]





        