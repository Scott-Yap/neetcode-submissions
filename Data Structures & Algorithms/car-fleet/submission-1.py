class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we loop from the back
        # we compare time to reach

        # create time to target stack
        cars = sorted(zip(position, speed))
        tot_stack = []

        for i in range(len(position) - 1, -1, -1):
            pos = cars[i][0]
            sp = cars[i][1]
            tot = (target - pos) / sp

            if tot_stack and tot <= tot_stack[-1]:
                tot = tot_stack[-1]
            
            tot_stack.append(tot)
        
        return len(set(tot_stack))