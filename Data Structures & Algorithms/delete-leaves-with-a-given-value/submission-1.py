# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        

        def isLeaf(root):
            if root is None :
                return False

            if root.right == None and root.left == None:
                return True 

            if isLeaf(root.right) and root.right.val == target:
                root.right = None 

            if isLeaf(root.left) and root.left.val == target:
                root.left = None

            return root.left is None and root.right is None 

        if isLeaf(root) and root.val == target:
            return None

        return root 