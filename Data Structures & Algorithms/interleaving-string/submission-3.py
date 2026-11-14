class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # top bottom
        # find which starts first 
        # then alternate
        # until the end then True
        # we going from right to left
        # solve(i,j) = can from remaing part of s3[:i+j+2] using s1[:i+1] and s2[:j+i]
        # at each step either from s1 or s2
        # either solve(i-1,j) or solve(i, j-1)
        # base is when i and j = -1 then return True

        mem = {}
        def solve(i,j):
            #base:
            if len(s1) + len(s2) != len(s3):
                return False
            if i==-1 and j==-1:
                return True
            
            if (i,j) in mem:
                return mem[(i,j)]
            
            if i >= 0 and s1[i]==s3[i+j+1]:
                if solve(i-1,j):
                    mem[(i,j)] = True
                    return mem[(i,j)]
            if j>=0 and s2[j]==s3[i+j+1]:
                if solve(i,j-1):
                    mem[(i,j)] = True
                    return mem[(i,j)]
            mem[(i,j)] = False
            return mem[(i,j)]
        return solve(len(s1)-1, len(s2)-1)

        

