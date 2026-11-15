class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6] -> forward product cum [1,2,8,48]
        # backward product cum [48,48,24,6]
        n=len(nums)
        forward = [1]*n
        backward = [1]*n
        res = [1]*n

        for i in range(n):
            if i==0:
                forward[i] = nums[i]
            else:
                forward[i] = forward[i-1] * nums[i]
        for j in range(n-1,-1,-1):
            if j==n-1:
                backward[j] = nums[j]
            else:
                backward[j] = backward[j+1] * nums[j]
        
        for k in range(n):
            if k==0:
                res[k] = backward[k+1]
            elif k==n-1:
                res[k] = forward[k-1]
            else:
                res[k] = forward[k-1] * backward[k+1]
        
        return res
            