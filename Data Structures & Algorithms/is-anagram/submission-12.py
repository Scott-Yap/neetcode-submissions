from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        track_s = Counter(s)
        track_t = Counter(t)

        return track_s == track_t