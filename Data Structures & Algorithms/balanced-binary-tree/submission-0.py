# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return is_Balanced_helper(root)[0]



def is_Balanced_helper(root):
    if root is None: return True, 0 

    right_is_balanced,right_len = is_Balanced_helper(root.right)
    left_is_balanced,left_len = is_Balanced_helper(root.left)

    if right_len != left_len and right_len != left_len+1 and  right_len +1 != left_len:
        return False,0 

    return (right_is_balanced and left_is_balanced),1 + max(right_len,left_len)

        