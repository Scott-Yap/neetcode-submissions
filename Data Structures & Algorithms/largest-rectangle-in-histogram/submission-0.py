class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use stack track the indices, it is used to find the max area for that indices, once popped mean found largest for that index
        # if next height is smaller then we pop the [-1] pop until find one that is smaller than the next height
        # at the we compute again

        # key idea: find the right index, left index then compute the area in between

        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                val = heights[stack.pop()]

                # compute the max area for that 
                right_ind = i
                if stack:
                    left_ind = stack[-1]
                else:
                    left_ind = -1
                
                max_area = max(max_area, val * (right_ind - left_ind - 1))
            else:
                stack.append(i)
            
        right_ind = len(heights)
        while stack:
            # compute max area 
            val = heights[stack.pop()]
            if stack:
                    left_ind = stack[-1]
            else:
                left_ind = -1
            max_area = max(max_area, val * (right_ind - left_ind - 1))
        
        return max_area


