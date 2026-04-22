# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        get_inorder_traversal(root, inorder)
        return inorder[k - 1 ]




def get_inorder_traversal(root, order):
    if not root : return 


    get_inorder_traversal(root.left,order)
    order.append(root.val)
    get_inorder_traversal(root.right, order)