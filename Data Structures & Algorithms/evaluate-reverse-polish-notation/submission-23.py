class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # O(n)
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a/b)
        }

        # O(1)
        result = 0

        # where 1 <= tokens.length <= 1000 => O(n) 
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])

        # run O(n)
        for token in tokens:
            if token in ops:
                right = stack.pop()
                left = stack.pop()  
                result = ops[token](left, right)
                stack.append(result)
            else:
                stack.append(int(token))
        return result 