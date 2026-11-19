class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        mem = {}
        def solve(i):
            if i == 0:
                return 0
            if i in mem:
                return mem[i]
            best = 0

            for j in range(1, min(k, i) + 1):
                score = max(arr[i-j:i]) * j + solve(i-j)
                best = max(best, score)
            mem[i] = best
            return best

        return solve(len(arr))
