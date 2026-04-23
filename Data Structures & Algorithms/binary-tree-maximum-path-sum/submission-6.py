# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(max_path_helper(root))


def max_path_helper(node):
    if node is None: return float("-inf") , float("-inf")


    right_diameter, right_height = max_path_helper(node.right)
    left_diameter , left_height = max_path_helper(node.left)
    curr_diameter = right_height + node.val + left_height 
    diameter_max = max(curr_diameter, right_diameter, left_diameter,node.val)
    height_max = max(node.val ,max(right_height,left_height) + node.val)


    return diameter_max,height_max