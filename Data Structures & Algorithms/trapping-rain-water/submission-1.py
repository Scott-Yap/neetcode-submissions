class Solution:
    def trap(self, height: List[int]) -> int:
        
        # # find leftmax and rightmax for each index

        # left_max = [0] * len(height)
        # right_max = [0] * len(height)

        # for i in range(1, len(height)):
        #     left_max[i] = max(left_max[i-1], height[i-1])

        # for j in range(len(height) - 2, -1, -1):
        #     right_max[j] = max(right_max[j+1], height[j+1])
        

        # # compute area for each index if both left max and right max bigger

        # area = 0

        # for i in range(1, len(height)-1):
        #     if left_max[i] > height[i] and right_max[i] > height[i]:
        #         area += min(left_max[i], right_max[i]) - height[i]
        
        # return area


        # using l r pointer to track left max and right max

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        area = 0

        while left < right:

            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                left += 1
                if left_max > height[left] and right_max > height[left]:
                    area += min(left_max, right_max) - height[left]
            
            else: 
                right -= 1
                if left_max > height[right] and right_max > height[right]:
                    area += min(left_max, right_max) - height[right]
            
        
        return area
            
            