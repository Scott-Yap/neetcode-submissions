class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        left = 0
        max_l = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            L = right - left + 1
            M = max(count.values())

            while right - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
                
            
            max_l = max(right - left + 1, max_l)
        
        return max_l
