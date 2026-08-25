class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""

        for word in strs:
            length = len(word)
            encode_str += str(length)
            encode_str += "#"
            encode_str += word

        return encode_str 


    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j + 1:length + j + 1]
            result.append(word)
            i = j + length + 1
        
        return result



