# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.order = []
        inorder_traversel(root,self.order)
        self.idx = 0

    def next(self) -> int:
        self.idx += 1 
        return self.order[self.idx-1]

    def hasNext(self) -> bool:
        return self.idx < len(self.order)
        

def inorder_traversel(node,res):
    if node is None :
        return 
    
    inorder_traversel(node.left,res)
    res.append(node.val)
    inorder_traversel(node.right,res)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()