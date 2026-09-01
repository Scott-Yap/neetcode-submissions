class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum_stack.append(min(self.minimum_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
