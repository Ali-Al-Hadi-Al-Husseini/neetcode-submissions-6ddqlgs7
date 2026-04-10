"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None :return None
        queue = [node]
        adj_list = []
        visited = set()

        while queue :
            curr_node = queue.pop()

            if curr_node.neighbors is None or curr_node in visited:
                continue
            idx = curr_node.val - 1 

            while len(adj_list)-1 < idx:
                adj_list.append([])

            for neigh in curr_node.neighbors:
                adj_list[idx].append(neigh.val)
                queue.append(neigh)
            visited.add(curr_node)

        nodes = [Node(val+1) for val in range(len(adj_list))]
        head= nodes[0]
        for idx,node in enumerate(nodes):
            neighbor = adj_list[idx]
            for val in neighbor:
                node.neighbors.append(nodes[val-1])

        return head
            
              