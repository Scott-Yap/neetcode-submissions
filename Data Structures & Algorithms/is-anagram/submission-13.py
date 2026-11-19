from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        track_s = dict()
        track_t = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            track_s[s[i]] = track_s.get(s[i], 0) + 1
            track_t[t[i]] = track_t.get(t[i], 0) + 1
        return track_s == track_t