# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(root,path_sum):
            if root is None:
                return 0 

            path_sum = path_sum * 10 + root.val
            if not root.left and not root.right:
                return path_sum

            return helper(root.left,path_sum,) + helper(root.right, path_sum)

        return  helper(root,0)