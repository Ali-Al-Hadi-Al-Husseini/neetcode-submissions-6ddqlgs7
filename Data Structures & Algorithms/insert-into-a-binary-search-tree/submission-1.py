# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr_node = root

        while curr_node:

            if val < curr_node.val:
                if  not curr_node.left :
                    curr_node.left = TreeNode(val)
                    break
                curr_node = curr_node.left
            else:
                if  not curr_node.right :
                    curr_node.right = TreeNode(val)
                    break
                curr_node = curr_node.right

        return root 
        