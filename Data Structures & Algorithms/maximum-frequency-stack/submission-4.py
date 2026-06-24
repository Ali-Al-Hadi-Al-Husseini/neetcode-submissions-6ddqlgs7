class FreqStack:

    def __init__(self):
        self.stacks = []
        self.freqs = defaultdict(int)

    def push(self, val: int) -> None:
        self.freqs[val] +=1 
        if self.freqs[val] > len(self.stacks):
            self.stacks.append([])
        self.stacks[self.freqs[val]-1].append(val)


    def pop(self) -> int:
        poped_val = self.stacks[-1].pop()
        self.freqs[poped_val] -= 1 

        if len(self.stacks[-1]) ==0 :
            self.stacks.pop()
            
        return poped_val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()