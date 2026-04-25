# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        max_depth = -1 

        def right_side_helper(node,curr_depth):
            if node is None:
                return 

            nonlocal max_depth
            if curr_depth > max_depth:
                res.append(node.val)

            max_depth = max(max_depth, curr_depth)
            # print(max_depth)

            right_side_helper(node.right,curr_depth +1)
            right_side_helper(node.left,curr_depth +1)

        right_side_helper(root,0)
        return res





