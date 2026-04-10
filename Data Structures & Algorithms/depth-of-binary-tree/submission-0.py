# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return maxDepth_helper(root)




def  maxDepth_helper(root):
    if root is None :return 0


    return 1 + max(maxDepth_helper(root.left), maxDepth_helper(root.right))
