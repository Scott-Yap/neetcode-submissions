class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # two dim dp
        # dp(i,j) : longest subseq txt1[:i+1], txt2[:j+1] 
        # i for text1 j for text 2
        # recursion, if match then we add 1 to dp(i-1,j-1)
        # if not pick the max from dp(i-1,j) or dp(i,j-1)


        mem = {}

        def solve(i,j):
            #base
            if i<0 or j<0:
                return 0
            
            if (i,j) in mem:
                return mem[(i,j)]

            if text1[i] == text2[j]:
                mem[(i,j)] = 1 + solve(i-1,j-1)
            else:
                mem[(i,j)] = max(solve(i-1,j), solve(i,j-1))
            
            return mem[(i,j)]
        
        return solve(len(text1)-1, len(text2)-1)
            