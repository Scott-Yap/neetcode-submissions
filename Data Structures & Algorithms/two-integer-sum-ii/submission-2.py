class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr = 0
        rptr = len(numbers) - 1

        while lptr < rptr:
            a = numbers[lptr]
            b = numbers[rptr]
            if a + b < target:
                lptr += 1
            elif a + b > target:
                rptr -= 1
            else:
                return [lptr + 1, rptr + 1]