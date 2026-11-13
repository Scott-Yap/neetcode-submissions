class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # find match then remove then remove until empty
        # State: solve(i) checks whether s[i:] can be segmented.
        #Base case: i == len(s) returns True.
        #Try each word that matches at position i.
        #Return False only after exhausting all choices.
        mem = {}
        def solve(i):
            if i == len(s):
                return True
            if i in mem:
                return mem[i]

            for word in wordDict:
                if s[i:].startswith(word):
                    if solve(i + len(word)):
                        mem[i] = True
                        return mem[i]
            mem[i]=False
            return mem[i]
        return solve(0)

