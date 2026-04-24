"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None:None}
        
        curr_node = head
        new_node = None
        while curr_node:
            if curr_node not in nodes:
                nodes[curr_node] = Node(curr_node.val)

            new_node = nodes[curr_node] 
            if curr_node.next != None :
                next_node = curr_node.next
                if next_node not in nodes:
                    nodes[next_node] = Node(next_node.val)
                new_node.next = nodes[next_node]

            if curr_node.random != None :
                random_node = curr_node.random
                if random_node not in nodes:
                    nodes[random_node] = Node(random_node.val)
                new_node.random  = nodes[random_node]           

            
            curr_node = curr_node.next

        return nodes[head]
