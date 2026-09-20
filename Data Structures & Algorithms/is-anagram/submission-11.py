class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = dict()
        counter_t = dict()

        for i in s:
            counter_s[i] = counter_s.get(i, 0) + 1

        for j in t:
            counter_t[j] = counter_t.get(j, 0) + 1

        return counter_s == counter_t
        