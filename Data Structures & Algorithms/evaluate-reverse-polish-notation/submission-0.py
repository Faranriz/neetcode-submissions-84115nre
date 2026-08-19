class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stack = []
        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(operators[token](left, right))
            else:
                stack.append(int(token))
        return stack[-1]