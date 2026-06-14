# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head

        i,j,n = 0,0, len(inorder)
        while i < n and j < n:
            
            curr.right = TreeNode(preorder[i],right=curr.right)
            curr = curr.right
            i += 1

            while i < n and curr.val != inorder[j]:
                new = TreeNode(preorder[i],right=curr)
                curr.left= new
                curr = new
                i += 1

            j += 1

            while curr.right and j < n and curr.right.val == inorder[j]:
                parent = curr.right
                curr.right = None
                curr = parent
                j += 1

        return head.right
