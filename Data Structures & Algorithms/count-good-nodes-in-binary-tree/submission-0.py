# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return good_nodes(root, float("-inf"))



def good_nodes(node, max_path):
    if node == None:
        return 0
    
    is_good = 1 if node.val >= max_path else 0
    new_max =  max(max_path,node.val)
    return is_good + good_nodes(node.left,new_max) + good_nodes(node.right,new_max)
    
