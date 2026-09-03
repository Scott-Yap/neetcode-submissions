class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)

        stack = [(temperatures[0], 0)]

        for ind in range(1, len(temperatures)):
            entry = (temperatures[ind], ind)
            while stack and temperatures[ind] > stack[-1][0]:
                out = stack.pop()
                result[out[1]] = ind - out[1]
            
            stack.append(entry)
            
        return result

