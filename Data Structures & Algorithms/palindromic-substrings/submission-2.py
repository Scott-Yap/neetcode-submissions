class Solution:
    def countSubstrings(self, s: str) -> int:
        # bottom up approach
        # dp[i] no of substring palindrom up to ind i

        # def valid(string):
        #     if len(string)%2==0:
        #         left = len(string)//2 - 1
        #         right = left + 1
        #     else:
        #         left = len(string)//2 
        #         right = left
                
        #     while left >=0 and right < len(string) and string[left]==string[right]:
        #         left -= 1
        #         right += 1
        #     left += 1
        #     right -= 1
        #     return left == 0 and right==len(string)-1

    
        # if len(s)==1:
        #     return 1
        # x1 = 2 + int(valid(s[0:2]))

        # for i in range(2, len(s)):
        #     count = 0
        #     for j in range(i-1,-1,-1):
        #         count += int(valid(s[j:i+1]))
        #     x1 = x1 + count + 1


        # return x1

        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # Last expansion failed, so move back to valid boundaries
            return count
        
        total = 0

        for i in range(len(s)):
            # Odd-length palindromes
            total += expand(i,i)

            # Even-length palindromes

            total += expand(i,i+1)

        return total

            
