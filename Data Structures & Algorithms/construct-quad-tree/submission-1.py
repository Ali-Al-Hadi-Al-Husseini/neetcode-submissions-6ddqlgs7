"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n= len(grid) -1

        def inbounds(coords):
            r,c= coords
            return n >= r >= 0 and n  >= c >= 0

        def tk(n,m):
            return (int(n),int(m))

        def helper(start,end):
            if start == end :
                r,c = start
                return Node(grid[r][c],True)

            if not inbounds(start) and not inbounds(end):
                print(start,end)
                return None


            new_node = None
            r,c = (start[0] + end[0]) / 2 ,(start[1] + end[1]) / 2 
            top_left = helper(tk(start[0],start[1]),tk(r-0.5,c-0.5))
            top_right = helper(tk(start[0],c+0.5),tk(r-0.5,end[1]))
            bottom_left = helper(tk(r+0.5,start[1]),tk(end[0],c-0.5))
            bottom_right =helper(tk(r+0.5,c+0.5),tk(end[0],end[1]))

            all_are_leafs = top_left.isLeaf and top_right.isLeaf and bottom_right.isLeaf and bottom_left.isLeaf
            all_have_same_val = top_left.val == top_right.val == bottom_right.val == bottom_left.val
            if all_are_leafs and all_have_same_val:
                new_node = Node(top_left.val,True)
            else:
                new_node =Node(top_left.val,
                                False,top_left,top_right,bottom_left,bottom_right)

            return new_node


        return helper((0,0),(n,n))


