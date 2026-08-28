class Solution:
    # def isPalindrome(self, s: str) -> bool:

    #     clean = "".join(char.lower() for char in s if char.isalnum())

    #     lptr = 0
    #     rptr = len(clean) - 1

    #     while lptr < rptr:
    #         if clean[lptr] != clean[rptr]:
    #             return False
    #         else:
    #             lptr += 1
    #             rptr -= 1
        
    #     return True

    def isPalindrome(self, s: str) -> bool:

        lptr = 0
        rptr = len(s) - 1

        while lptr < rptr:
            if not s[lptr].isalnum():
                lptr += 1
            elif not s[rptr].isalnum():
                rptr -= 1
            elif s[rptr].lower() == s[lptr].lower():
                lptr += 1
                rptr -= 1
            else:
                return False
        
        return True
                