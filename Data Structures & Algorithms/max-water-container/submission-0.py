class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use two pointer, then shift when area is larger

        lptr = 0
        rptr = len(heights) - 1
        max_vol = min(heights[lptr], heights[rptr]) * (rptr - lptr)

        while lptr < rptr:
            a = heights[lptr]
            b = heights[lptr + 1]
            c = heights[rptr - 1]
            d = heights[rptr]

            if a >= d:
                max_vol = max(max_vol, min(a,c) * (rptr - 1 - lptr))
                rptr -= 1
            
            elif a < d:
                max_vol = max(max_vol, min(b,d) * (rptr - 1 - lptr))
                lptr += 1
            
        return max_vol

