class MinStack:

    def __init__(self):
        self.stack = []
        self.minT = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minT:
            self.minT.append(val)
        else:
            if self.minT[-1] > val:
                self.minT.append(val)
            else:
                self.minT.append(self.minT[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minT.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minT[-1]
        
