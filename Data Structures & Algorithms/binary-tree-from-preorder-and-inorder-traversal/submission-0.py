# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx,j = 0,0

        def dfs(limit):
            nonlocal idx,j
            if idx >= len(preorder) :
                return 
            if inorder[j] == limit:
                j += 1
                return 

            root = TreeNode(preorder[idx])
            idx +=1 
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root

        return dfs(float("inf"))