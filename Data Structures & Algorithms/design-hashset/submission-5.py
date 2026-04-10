class MyHashSet:

    def __init__(self):
        self.amount = 10**6
        self.arr = [0] * (self.amount // 32)

    def add(self, key: int) -> None:
        self.arr[key // 32] |= self.get_bit_mask(key)

    def remove(self, key: int) -> None:
        self.arr[key // 32] &= ~self.get_bit_mask(key)
        

    def contains(self, key: int) -> bool:
        return (self.arr[key // 32] & self.get_bit_mask(key)) != 0  
        
    def get_bit_mask(self,key):
        return 1 << (key % 32)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)