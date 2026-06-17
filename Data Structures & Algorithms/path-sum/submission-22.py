# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(node, path_sum):
            if node is None :
                return False
            path_sum += node.val 
            if node.left is None and node.right is None:
                return path_sum == targetSum
     
            return helper(node.left,path_sum) or helper(node.right,path_sum)

        return helper(root,0)
