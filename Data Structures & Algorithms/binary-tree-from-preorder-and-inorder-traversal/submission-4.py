# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx,self.in_idx = 0 ,0 

        def build(stop_val):
            if self.pre_idx >= len(preorder):
                return 
            if inorder[self.in_idx] == stop_val:
                self.in_idx += 1 
                return 

            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1 
            root.left = build(root.val)
            root.right = build(stop_val)
            return root
            
        return build(float("inf"))