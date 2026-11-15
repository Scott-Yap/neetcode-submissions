class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # word1 and word2
        # three ops on word1
        # insert, delete, replace
        # min ops to make word1 equal word2
        # dp[i,j] = min operations of word1[:i+1] to match word2[:j+1]
        # recurrance
        # insert: ab vs abc dp(i,j-1) + 1 (after insert which is resolved) abc, abc -> ab,ab
        # delete: abcd vs abc dp(i-1,j) + 1
        # replace: abd vs abc dp(i-1,j-1) + 1
        # match: dp(i-1,j-1)
        # base: if i ==-1, means word2 is still here so its just inserting j+1
        # base if j==-1, means word2 empty so need to remove i+1
        mem = {}

        def solve(i,j):
            if i == -1:
                return j + 1

            if j == -1:
                return i + 1
            
            if (i,j) in mem:
                return mem[(i,j)]
            
            if word1[i] == word2[j]:
                mem[(i,j)] = solve(i-1,j-1)
            
            else:
                mem[(i,j)] = 1 + min(solve(i-1,j), solve(i-1,j-1), solve(i,j-1))
            return mem[(i,j)]
        
        return solve(len(word1)-1,len(word2)-1)
            