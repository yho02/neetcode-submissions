class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == '+':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(a+b)
            elif token == '*':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(a*b)
            elif token == '-':
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a-b)
            elif token == '/':
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(int(a/b))
            else:
                stack.append(int(token))
        return int(stack[0])