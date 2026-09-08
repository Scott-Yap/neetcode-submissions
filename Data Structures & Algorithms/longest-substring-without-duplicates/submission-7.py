class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointer left and right 
        if not s:
            return 0

        left_ptr = 0
        right_ptr = 1
        seen = dict()
        seen[s[left_ptr]] = left_ptr

        max_length = 1

        while right_ptr < len(s):

            if s[right_ptr] in seen:
                if seen[s[right_ptr]] >= left_ptr:
                    left_ptr = seen[s[right_ptr]] + 1
                
            max_length = max(max_length, right_ptr - left_ptr + 1)
            
            seen[s[right_ptr]] = right_ptr
            
            right_ptr += 1
        
        
        return max_length