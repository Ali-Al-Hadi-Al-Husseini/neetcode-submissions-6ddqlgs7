# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True  
        if not root:
            return False

        if self.sameTree(root,subRoot):
            return True
        
        check_left = self.isSubtree(root.left,subRoot)
        check_right = self.isSubtree(root.right,subRoot)

        return check_left or check_right


    def sameTree(self,tree,subTree):
        if tree is None and subTree is None:
            return True

        if tree and subTree and tree.val == subTree.val:
            left_is_same  = self.sameTree(tree.left,subTree.left)
            right_is_same = self.sameTree(tree.right,subTree.right)
            
            return left_is_same and right_is_same

        return False 