class MyHashSet:

    def __init__(self):
        self.len = 10 **4
        self.arr = [None] * self.len
        
    def add(self, key: int) -> None:
        index = key % self.len
        if not self.arr[index]:
            self.arr[index] = key

    def remove(self, key: int) -> None:
        index = key % self.len
        self.arr[index] = None
        

    def contains(self, key: int) -> bool:
        index = key % self.len
        if not self.arr[index]:
            return False
        return True     


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)