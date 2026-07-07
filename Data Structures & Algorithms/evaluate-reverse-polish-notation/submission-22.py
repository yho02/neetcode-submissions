class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a/b)
        }

        result = 0
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token in ops:
                print(stack)
                right = stack.pop()
                left = stack.pop()  
                print(type(left), type(right))           
                result = ops[token](left, right)
                stack.append(result)
            else:
                stack.append(int(token))
        return result 