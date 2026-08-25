# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # hashmap counter
#         counter = {}

#         for i in nums:
#             counter[i] = counter.get(i, 0) + 1

#         sorted_keys = sorted(counter, key=lambda x: counter[x], reverse=True)

#         return sorted_keys[:k]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap counter
        counter = {}

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        
        # bubble sort
        buckets = [[] for _ in range(len(nums)+1)]

        for key in counter:
            buckets[counter[key]].append(key)
        
        result = []
        for i in range(len(buckets)-1, -1 , -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result