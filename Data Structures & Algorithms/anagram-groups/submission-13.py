from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        
        for ind in range(len(strs)):
            word = strs[ind]
            count_word = [0] * 26
            for char in word:
                count_word[ord(char) - ord("a")] += 1
            
            count[tuple(count_word)].append(word)

        return list(count.values())

