class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if  self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
    

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1] if len(self) else None

    def getMin(self) -> int:
        return self.min_stack[-1] if len(self) else None
        
    def __len__(self):
        return len(self.stack)
