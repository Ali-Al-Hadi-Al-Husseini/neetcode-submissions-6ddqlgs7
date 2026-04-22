# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_binary_tree(root,float("-inf"),float("+inf"))





def is_binary_tree(root,left_max,right_min):
    if root == None :return True
    if not (left_max < root.val < right_min):
        return False

    return is_binary_tree(root.left,left_max,root.val) and is_binary_tree(root.right,root.val,right_min)





