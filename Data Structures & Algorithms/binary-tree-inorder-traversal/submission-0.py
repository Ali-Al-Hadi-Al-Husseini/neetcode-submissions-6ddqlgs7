# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        get_order(root,order)
        return order 



def get_order(root,order):
    if root is None : return 

    get_order(root.left,order)
    order.append(root.val)
    get_order(root.right, order)