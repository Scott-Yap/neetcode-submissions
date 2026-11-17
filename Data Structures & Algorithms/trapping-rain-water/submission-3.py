class Solution:
    def trap(self, height: List[int]) -> int:
        # how to trap water
        # we need to have middle less than the boundary
        # from left to right: if right smaller than will have trap
        # from right to left: if left smaller than trap
        # 203 -> left max 2, right max 3 middle 0 so we take the min of the boundary * length which is right - left -1
        # then 3,1,0,1,3. left = 3 right = 3 3,1 -> 2 3,0 -> 3 
        # 3,1 -> 2, 3,3 -> 0 -> total 7
        # but i think we can still do left = 0 right = len -1 

        # simple case track left and right 
        left = 0
        right = len(height) - 1
        volume = 0
        left_max = 0
        right_max = 0

        while left < right: 
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            volume += left_max - height[left]
            volume += right_max - height[right]

            # if left higher, move right
            if left_max > right_max:
                right -= 1
            else:
                left += 1

        return volume


