# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 
        def helper(root):
            nonlocal res 
            if not root : 
                return 0

            max_left = helper(root.left)
            max_right = helper(root.right)

            res = max(res, max_right + max_left) 
            return 1+ max(max_left,max_right)

        helper(root)
        return res




