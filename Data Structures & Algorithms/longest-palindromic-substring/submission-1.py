class Solution:
    def longestPalindrome(self, s: str) -> str:
        # longestpalindrom
        # loop through all cetres
        max_length = 0
        max_track = ""
        for i in range(len(s)):
            left, right = i,i

            while left>=0 and right<len(s) and s[left]==s[right]:
                
                
                length = right-left+1
                if length > max_length:
                    max_length = length
                    max_track = s[left:right+1]

                left-=1
                right+=1
            left2, right2 = i,i+1
            while left2>=0 and right2<len(s) and s[left2]==s[right2]:
                
               
                length = right2-left2+1
                if length > max_length:
                    max_length = length
                    max_track = s[left2:right2+1]
                left2-=1
                right2+=1
        return max_track
                

