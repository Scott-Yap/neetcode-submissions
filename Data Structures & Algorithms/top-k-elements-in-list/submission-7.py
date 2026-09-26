class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = dict()

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        sorted_keys = sorted(count_dict, key=lambda x: count_dict[x], reverse=True)

        return sorted_keys[:k]