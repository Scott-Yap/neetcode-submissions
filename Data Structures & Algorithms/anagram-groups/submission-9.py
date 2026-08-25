class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # convert all words into frequency list
        # change that into tuple to be used as key in the hashmap, and value would be the word
        # output the values out

        # convert
        result = {}

        for word in strs:
            freq = [0] * 26
            
            for char in word:
                freq[ord(char) - ord('a')] += 1

            key = tuple(freq)
            
            if key in result:
                result[key].append(word)
            else:
                result[key] = [word]
        
        return [result[i] for i in result]
