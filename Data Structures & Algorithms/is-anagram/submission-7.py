class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        t_counter = {}

        for i in s:
            if i in s_counter:
                s_counter[i] += 1
            else:
                s_counter[i] = 1

        for j in t:
            if j in t_counter:
                t_counter[j] += 1
            else:
                t_counter[j] = 1

        return s_counter == t_counter