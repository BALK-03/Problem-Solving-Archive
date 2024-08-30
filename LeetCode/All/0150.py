class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Pay attention
        # In Python 2, the / operator performs integer division, and rounds towards negative infinity.
                    # So 6/-132 gives -1, and of course int(6/-132) also gives -1.

        # In Python 3, the / operator performs float division, so 6/-132 is -0.045.
                    # Then the int function truncates decimals, so int(6/-132) is 0.
        oper = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        stack = []
        
        for token in tokens:
            if token not in oper:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                result = oper[token](num1, num2)
                stack.append(result)
        
        return stack.pop()