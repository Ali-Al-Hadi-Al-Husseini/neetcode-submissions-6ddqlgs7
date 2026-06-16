class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None 

class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None 

    def remove(self,node):
        is_head_or_tail = False
        if node is self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            is_head_or_tail = True
        if self.tail is node:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            is_head_or_tail = True
        if is_head_or_tail:
            return
             
             
        print(node.key)
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add(self,node):
        if not self.tail:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


class LRUCache:

    def __init__(self, capacity: int):
        self.ll = Doubly_linked_list()
        self.capacity = capacity
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        node = self.cache[key][1]
        self.ll.remove(node)
        self.ll.add(node)

        return self.cache[key][0]
        
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key][1]
            self.ll.remove(node)

        node = Node(key)
        self.cache[key] = (value, node)
        self.ll.add(node)
        
        if len(self.cache) > self.capacity:
            del self.cache[self.ll.head.key]

            self.ll.remove(self.ll.head)

