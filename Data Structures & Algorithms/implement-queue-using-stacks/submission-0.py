class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        self.s2 = list(reversed(self.s1))

    def pop(self) -> int:
        pop_val = self.s2.pop()

        self.s1 = list(reversed(self.s2))

        return pop_val

    def peek(self) -> int:
        return self.s2[-1]
        

    def empty(self) -> bool:
        return (len(self.s1) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()