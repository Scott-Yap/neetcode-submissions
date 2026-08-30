class Solution:
    def trap(self, height: List[int]) -> int:
        
        # find leftmax and rightmax for each index

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])

        for j in range(len(height) - 2, -1, -1):
            right_max[j] = max(right_max[j+1], height[j+1])
        

        # compute area for each index if both left max and right max bigger

        area = 0

        for i in range(1, len(height)-1):
            if left_max[i] > height[i] and right_max[i] > height[i]:
                area += min(left_max[i], right_max[i]) - height[i]
        
        return area