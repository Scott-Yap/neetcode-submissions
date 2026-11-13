# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        # longestpalindrom
        # loop through all cetres
        # max_length = 0
        # max_track = ""
        # for i in range(len(s)):
        #     left, right = i,i

        #     while left>=0 and right<len(s) and s[left]==s[right]:
                
                
        #         length = right-left+1
        #         if length > max_length:
        #             max_length = length
        #             max_track = s[left:right+1]

        #         left-=1
        #         right+=1
        #     left2, right2 = i,i+1
        #     while left2>=0 and right2<len(s) and s[left2]==s[right2]:
                
               
        #         length = right2-left2+1
        #         if length > max_length:
        #             max_length = length
        #             max_track = s[left2:right2+1]
        #         left2-=1
        #         right2+=1
        # return max_track
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best_left, best_right = 0, 0

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            # Last expansion failed, so move back to valid boundaries
            return left + 1, right - 1

        for i in range(n):
            # Odd-length palindrome
            left, right = expand(i, i)
            if right - left > best_right - best_left:
                best_left, best_right = left, right

            # Even-length palindrome
            left, right = expand(i, i + 1)
            if right - left > best_right - best_left:
                best_left, best_right = left, right

        return s[best_left:best_right + 1]



