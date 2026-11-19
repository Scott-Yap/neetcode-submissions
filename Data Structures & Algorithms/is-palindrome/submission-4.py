class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ''.join(c.lower() for c in s if c.isalnum())

        # expand through centre
        # if even pair is n//2-1 n//2 
        # if odd n//2

        n = len(s_clean)
        if n%2==0:
            left = n//2-1
            right = n//2
        else:
            left = n//2
            right = n//2

        
        while left>=0 and right<n:
            if s_clean[left]!= s_clean[right]:
                return False
            
            left -=1
            right +=1
        
        return True