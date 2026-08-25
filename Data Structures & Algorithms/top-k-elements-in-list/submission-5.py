class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap counter
        counter = {}

        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        sorted_keys = sorted(counter, key=lambda x: counter[x], reverse=True)

        return sorted_keys[:k]



        