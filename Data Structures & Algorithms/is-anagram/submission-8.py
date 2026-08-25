class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        t_counter = {}

        for i in s:
            s_counter[i] = s_counter.get(i, 0) + 1

        for j in t:
            t_counter[j] = t_counter.get(j, 0) + 1

        return s_counter == t_counter