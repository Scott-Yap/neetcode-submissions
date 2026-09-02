class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        operator_dict = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
            }
        
        for i in tokens:
            if i not in operator_dict:
                num.append(int(i))
            else:
                second = num.pop()
                first = num.pop()
                num.append(operator_dict[i](first, second))
        
        return num[-1]