class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = "".join(char.lower() for char in s if char.isalnum())

        lptr = 0
        rptr = len(clean) - 1

        while lptr < rptr:
            if clean[lptr] != clean[rptr]:
                return False
            else:
                lptr += 1
                rptr -= 1
        
        return True
                