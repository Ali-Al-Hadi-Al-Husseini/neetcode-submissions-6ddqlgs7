class MinStack:

    def __init__(self):
        self.tail = None 
        self.min_tail =  Node(float("+inf"))

    def push(self, val: int) -> None:
        if self.tail :
            new_node = Node(val)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.tail = Node(val)

        new_min_node = Node(min(val,self.min_tail.val))
        self.min_tail.next = new_min_node
        new_min_node.prev = self.min_tail
        self.min_tail = new_min_node
        
    def pop(self) -> None:
        if  self.tail.prev:  
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node

        prev_node = self.min_tail.prev
        prev_node.next = None
        self.min_tail = prev_node

    def top(self) -> int:
        return self.tail.val

    def getMin(self) -> int:
        return self.min_tail.val


class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()