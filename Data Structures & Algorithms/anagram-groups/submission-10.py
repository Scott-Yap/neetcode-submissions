# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # transform each word to numeric tuple
#         groups = {}

#         for i in strs:
#             count = [0] * 26
#             for j in i:
#                 count[ord(j) -  ord('a')] += 1
#             count = tuple(count)
#             if count in groups:
#                 groups[count].append(i)
#             else:
#                 groups[count] = [i]
            
#         return list(groups.values())


    

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())