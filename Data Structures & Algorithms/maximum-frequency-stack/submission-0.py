class FreqStack:

    def __init__(self):
        self.heap = []
        self.freqs = defaultdict(int)
        self.size = 0
    def push(self, val: int) -> None:
        self.freqs[val] -= 1
        self.size -=1 
        heapq.heappush(self.heap,(self.freqs[val],self.size,val))

    def pop(self) -> int:
        _,_,poped_val =heapq.heappop(self.heap)
        self.freqs[poped_val] += 1
        self.size += 1
        if self.freqs[poped_val] >=0 :
            del self.freqs[poped_val]
        return poped_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()