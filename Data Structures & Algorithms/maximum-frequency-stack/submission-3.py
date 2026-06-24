class FreqStack:

    def __init__(self):
        self.stack_map = defaultdict(list)
        self.freqs = defaultdict(int)

    def push(self, val: int) -> None:
        self.freqs[val] +=1 
        self.stack_map[self.freqs[val]].append(val)


    def pop(self) -> int:
        max_freq = len(self.stack_map)
        poped_val = self.stack_map[max_freq].pop()
        self.freqs[poped_val] -= 1 


        if len(self.stack_map[max_freq]) ==0 :
            del self.stack_map[max_freq]

        return poped_val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()