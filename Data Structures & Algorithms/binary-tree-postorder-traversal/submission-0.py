# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        make_order(root,order)
        return order 


def make_order(root, order):
    if not root : return 

    make_order(root.left, order)
    make_order(root.right, order)
    order.append(root.val)
