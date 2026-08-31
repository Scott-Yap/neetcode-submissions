class Solution:
    def isValid(self, s: str) -> bool:
        val = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        res = []

        for i in s:

            if i in val.values():
                if not res:
                    return False
                if val[res[-1]] == i:
                    res.remove(res[-1])
                else:
                    return False
            
            else:
                res.append(i)
            
        return not res
