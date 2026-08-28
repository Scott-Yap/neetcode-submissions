class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort nums
        # fix nums[i]
        # then use two pointers on everything after i

        result = [] 
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lptr = i + 1
            rptr = len(nums) - 1

            while lptr < rptr:
                if nums[i] + nums[lptr] + nums[rptr] < 0:
                    lptr += 1
                elif nums[i] + nums[lptr] + nums[rptr] > 0:
                    rptr -= 1
                else:
                    result.append([nums[i], nums[lptr], nums[rptr]])
                    lptr += 1
                    rptr -= 1

                    while lptr < rptr and nums[lptr] == nums[lptr - 1]:
                        lptr += 1
                    while lptr < rptr and nums[rptr] == nums[rptr + 1]:
                        rptr -= 1
        
        return result
